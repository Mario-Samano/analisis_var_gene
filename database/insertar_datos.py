from pathlib import Path
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv("credenciales.env")

# ============================================================
# 0. Configuración de rutas y credenciales
# ============================================================
BASE_DIR = Path("/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene")
NEXTCLADE_DIR = BASE_DIR / "results" / "nextclade"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
YEARS = [2020, 2021, 2022, 2023, 2024]



conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()

# Helper para convertir NaN → None (NULL en MySQL)
def clean(value):
    if pd.isna(value):
        return None
    return value

# ============================================================
# 1. Insertar secuencias (desde los TSV de Nextclade)
# ============================================================
print("Insertando secuencias...")
total_seqs = 0
for year in YEARS:
    path = NEXTCLADE_DIR / f"nextclade_{year}.tsv"
    if not path.exists():
        print(f"  [WARN] No existe {path}, se omite.")
        continue
    nc = pd.read_csv(path, sep="\t")
    query = """
    INSERT INTO secuencias (seq_name, year, clade, clade_who, qc_status, total_missing)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE year=VALUES(year)
    """
    for _, row in nc.iterrows():
        cursor.execute(query, (
            row["seqName"], year,
            clean(row.get("clade")),
            clean(row.get("clade_who")),
            clean(row.get("qc.overallStatus")),
            clean(row.get("qc.missingData.totalMissing"))
        ))
    conn.commit()
    total_seqs += len(nc)
    print(f"  {year}: {len(nc)} secuencias")
print(f"  Total: {total_seqs} secuencias insertadas.")

# ============================================================
# 2. Insertar mutaciones
# ============================================================
print("Insertando mutaciones...")
df_muts = pd.read_csv(PROCESSED_DIR / "nuevas_mutaciones_clasificadas.tsv", sep="\t")
query = """
INSERT INTO mutaciones (seq_name, year, mutation, position, gene, codon, aa_mutation, type)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
for _, row in df_muts.iterrows():
    cursor.execute(query, (
        row["seqName"], int(row["year"]), row["mutation"], int(row["position"]),
        clean(row.get("gene")),
        clean(row.get("codon")),
        clean(row.get("aa_mutation")),
        clean(row.get("type"))
    ))
conn.commit()
print(f"  {len(df_muts)} mutaciones insertadas.")

# ============================================================
# 3. Insertar frecuencias AA
# ============================================================
print("Insertando frecuencias AA...")
df_freq_aa = pd.read_csv(PROCESSED_DIR / "nuevas_frecuencias_aa_por_anio.tsv",
                         sep="\t", index_col=[0, 1])
for (aa_mut, gene), row in df_freq_aa.iterrows():
    for year in YEARS:
        if str(year) in df_freq_aa.columns:
            cursor.execute(
                "INSERT INTO frecuencias_aa (aa_mutation, gene, year, frequency) "
                "VALUES (%s, %s, %s, %s) "
                "ON DUPLICATE KEY UPDATE frequency=VALUES(frequency)",
                (clean(aa_mut), clean(gene), year, clean(float(row[str(year)])))
            )
conn.commit()
print("  Frecuencias AA insertadas.")

# ============================================================
# 4. Insertar frecuencias NT
# ============================================================
print("Insertando frecuencias NT...")
df_freq_nt = pd.read_csv(PROCESSED_DIR / "nuevas_frecuencias_nt_por_anio.tsv",
                         sep="\t", index_col=[0, 1])
for (mut, gene), row in df_freq_nt.iterrows():
    for year in YEARS:
        if str(year) in df_freq_nt.columns:
            cursor.execute(
                "INSERT INTO frecuencias_nt (mutation, gene, year, frequency) "
                "VALUES (%s, %s, %s, %s) "
                "ON DUPLICATE KEY UPDATE frequency=VALUES(frequency)",
                (clean(mut), clean(gene), year, clean(float(row[str(year)])))
            )
conn.commit()
print("  Frecuencias NT insertadas.")

# ============================================================
# 5. Insertar densidad por gen
# ============================================================
print("Insertando densidad por gen...")
df_density = pd.read_csv(PROCESSED_DIR / "nueva_densidad_por_gen.tsv", sep="\t")
for _, row in df_density.iterrows():
    cursor.execute(
        """
        INSERT INTO densidad_por_gen (gene, length_nt, unique_mutations, mutations_per_kb)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE mutations_per_kb=VALUES(mutations_per_kb)
        """,
        (clean(row["gene"]), int(row["length_nt"]),
         int(row["unique_mutations"]), float(row["mutations_per_kb"]))
    )
conn.commit()
print(f"  {len(df_density)} genes insertados.")

# ============================================================
# 6. Insertar resultados estadísticos
# ============================================================
print("Insertando resultados estadísticos...")
for nivel, archivo in [("AA", "resultados_estadisticos_aa.tsv"),
                       ("NT", "resultados_estadisticos_nt.tsv")]:
    path = PROCESSED_DIR / archivo
    if not path.exists():
        print(f"  [WARN] No existe {path}, se omite.")
        continue
    df_stats = pd.read_csv(path, sep="\t")
    for _, row in df_stats.iterrows():
        cursor.execute(
            """
            INSERT INTO resultados_estadisticos
            (mutation, gene, nivel, delta, p_value_periodos,
             coef_year, odds_ratio, p_value_tendencia,
             significativo_periodos, significativo_tendencia, direccion)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                clean(row["mutation"]), clean(row["gene"]), nivel,
                clean(row.get("delta")),
                clean(row.get("p_value_periodos")),
                clean(row.get("coef_year")),
                clean(row.get("odds_ratio")),
                clean(row.get("p_value_tendencia")),
                bool(row.get("significativo_periodos", False)),
                bool(row.get("significativo_tendencia", False)),
                clean(row.get("direccion"))
            )
        )
    conn.commit()
    print(f"  {nivel}: {len(df_stats)} resultados insertados.")

# ============================================================
# Cierre
# ============================================================
cursor.close()
conn.close()
print("\nDatos insertados correctamente.")