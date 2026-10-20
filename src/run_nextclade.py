# src/run_nextclade.py
import subprocess

# Rutas absolutas del proyecto
DATASET_DIR = "/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene/data/sars-cov-2"
RAW_DIR = "/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene/data/raw"
REFERENCE_FASTA = "/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene/data/raw/reference/wuhan_ref.fasta"
NEXTCLADE_DIR = "/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene/results/nextclade"


def descargar_dataset_sars_cov2(output_dir=DATASET_DIR):
    """Descarga el dataset de SARS-CoV-2 de Nextclade."""
    print("Descargando dataset de SARS-CoV-2")

    # ----------------------------------------------------------------- Comando equivalente a correr "nextclade dataset get" en la terminal
    cmd = ["nextclade", "dataset", "get","--name", "nextstrain/sars-cov-2/wuhan-hu-1/orfs","--output-dir", output_dir,]

    # ----------------------------------------------------------------- capture_output guarda stdout y stderr; text=True los devuelve como str
    resultado = subprocess.run(cmd, capture_output=True, text=True)

    # ----------------------------------------------------------------- confirmación de éxito
    print(f"[OK] Dataset descargado en {output_dir}")



def alinear_año(año, input_fasta, output_tsv, output_fasta, dataset_dir=DATASET_DIR, reference_fasta=None):
    """Ejecuta Nextclade para un año específico usando una referencia propia."""

    # ----------------------------------------------------------------- Comando base: dataset de entrada y archivos de salida (TSV y FASTA alineado)
    cmd = ["nextclade", "run","--input-dataset", dataset_dir,"--output-tsv", output_tsv,"--output-fasta", output_fasta,]

    # ----------------------------------------------------------------- Referencia propia en lugar de la que trae el dataset
    cmd.extend(["--input-ref", reference_fasta])

    # ----------------------------------------------------------------- El FASTA con los genomas a alinear va al final, como argumento posicional
    cmd.append(input_fasta)

    # ----------------------------------------------------------------- split('/')[-1] deja solo el nombre del archivo, sin la ruta
    print(f"[ALIGN] Año {año}: {input_fasta.split('/')[-1]}")
    resultado = subprocess.run(cmd, capture_output=True, text=True)

    if resultado.returncode == 0:
        print(f"[OK] Año {año} completado -> {output_tsv.split('/')[-1]}")
        return True
    else:
        # ------------------------------------------------------------- Solo los primeros 500 caracteres del error para no inundar la salida
        print(f"[ERROR] Año {año}: {resultado.stderr[:500]}")
        return False