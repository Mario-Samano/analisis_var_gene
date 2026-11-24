import os
from pathlib import Path

import mysql.connector
import pandas as pd
from dotenv import load_dotenv

BASE_DIR = Path("/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene")
load_dotenv(BASE_DIR / "PracticaDB" / "credenciales.env")

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()


def print_query(title, query):
    """Ejecuta una consulta y la imprime como tabla."""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    print(df.to_string(index=False))
    return df


# ============================================================
# RESULTADOS ESTADÍSTICOS: VISTA COMPLETA
# ============================================================
print_query(
    "TODOS los resultados estadísticos (AA)",
    """
    SELECT mutation, gene, delta, p_value_periodos,
           coef_year, odds_ratio, p_value_tendencia,
           significativo_periodos, significativo_tendencia, direccion
    FROM resultados_estadisticos
    WHERE nivel = 'AA'
    ORDER BY p_value_periodos ASC
    """
)

print_query(
    "TODOS los resultados estadísticos (NT)",
    """
    SELECT mutation, gene, delta, p_value_periodos,
           coef_year, odds_ratio, p_value_tendencia,
           significativo_periodos, significativo_tendencia, direccion
    FROM resultados_estadisticos
    WHERE nivel = 'NT'
    ORDER BY p_value_periodos ASC
    """
)

# ============================================================
# RESPUESTA A PREGUNTA 2: ¿qué mutaciones cambiaron significativamente?
# ============================================================
print_query(
    "Mutaciones que cambiaron significativamente entre 2021 y 2022 (p < 0.05)",
    """
    SELECT mutation, gene, nivel, delta, p_value_periodos, direccion
    FROM resultados_estadisticos
    WHERE significativo_periodos = TRUE
    ORDER BY delta DESC
    """
)

print_query(
    "Mutaciones con tendencia temporal significativa (p < 0.05)",
    """
    SELECT mutation, gene, nivel, coef_year, odds_ratio, p_value_tendencia, direccion
    FROM resultados_estadisticos
    WHERE significativo_tendencia = TRUE
    ORDER BY odds_ratio DESC
    """
)

# ============================================================
# RESPUESTA A PREGUNTA 1: densidad por gen
# ============================================================
print_query(
    "Genes con mayor densidad de mutaciones",
    """
    SELECT gene, length_nt, unique_mutations, mutations_per_kb
    FROM densidad_por_gen
    ORDER BY mutations_per_kb DESC
    """
)

# ============================================================
# CRUZAR RESULTADOS: mutaciones significativas en genes clave
# ============================================================
print_query(
    "Mutaciones significativas en Spike (S)",
    """
    SELECT mutation, delta, p_value_periodos, odds_ratio, p_value_tendencia, direccion
    FROM resultados_estadisticos
    WHERE gene = 'S' AND significativo_periodos = TRUE
    ORDER BY delta DESC
    """
)

print_query(
    "Mutaciones significativas en ORF1a y ORF1b",
    """
    SELECT mutation, gene, delta, p_value_periodos, odds_ratio, direccion
    FROM resultados_estadisticos
    WHERE gene IN ('ORF1a', 'ORF1b') AND significativo_periodos = TRUE
    ORDER BY delta DESC
    """
)

# ============================================================
# CONTEXTO: secuencias por año
# ============================================================
print_query(
    "Número de secuencias por año (contexto del análisis)",
    """
    SELECT year, COUNT(*) AS n_secuencias
    FROM secuencias
    GROUP BY year
    ORDER BY year
    """
)

# ============================================================
# CIERRE
# ============================================================
cursor.close()
conn.close()
print("\nConsultas ejecutadas correctamente.")