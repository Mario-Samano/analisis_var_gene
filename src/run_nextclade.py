import subprocess

# -------------------------------------------------------------------- Rutas absolutas del proyecto
DATASET_DIR = "/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene/data/sars-cov-2"
RAW_DIR = "/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene/data/raw"
REFERENCE_FASTA = "/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene/data/raw/reference/wuhan_ref.fasta"
NEXTCLADE_DIR = "/export/space3/users/mariosb/LCG/BIOPYTHON/analisis_var_gene/results/nextclade"


def descargar_dataset_sars_cov2(output_dir=DATASET_DIR):
    """Descarga el dataset de SARS-CoV-2 de Nextclade.

    Ejecuta "nextclade dataset get" con el dataset
    nextstrain/sars-cov-2/wuhan-hu-1/orfs y lo guarda en output_dir.
    Si el ejecutable nextclade no se encuentra, imprime un error y
    termina sin descargar nada.

    Args:
        output_dir: Ruta absoluta de la carpeta donde se guarda el dataset. Por defecto: DATASET_DIR.

    Returns:
        None.
    """
    print("Descargando dataset de SARS-CoV-2")

    # ----------------------------------------------------------------- Comando equivalente a correr "nextclade dataset get" en la terminal
    cmd = ["nextclade", "dataset", "get","--name", "nextstrain/sars-cov-2/wuhan-hu-1/orfs","--output-dir", output_dir,]

    # ----------------------------------------------------------------- capture_output guarda stdout y stderr; text=True los devuelve como str
    try: 
        resultado = subprocess.run(cmd, capture_output=True, text=True)
    # ------------------------------------------------------------- subprocess lanza FileNotFoundError si el ejecutable nextclade no está en el PATH
    except FileNotFoundError as error:
        print(f"[ERROR] No se encontró: {error.filename}")
        return

    print(f"[LISTO] Dataset descargado en {output_dir}")



def alinear_año(año, input_fasta, output_tsv, output_fasta, dataset_dir=DATASET_DIR, reference_fasta=None):
    """Ejecuta Nextclade para un año específico usando una referencia propia.

    Alinea los genomas de input_fasta contra reference_fasta con
    "nextclade run" y guarda los resultados en un TSV y un FASTA
    alineado. Antes de ejecutar, verifica que existan el FASTA de
    entrada, la referencia y el dataset.

    Args:
        año: Año de los genomas. Solo se usa en los mensajes.
        input_fasta: Ruta absoluta del FASTA con los genomas a alinear.
        output_tsv: Ruta absoluta del TSV de resultados.
        output_fasta: Ruta absoluta del FASTA alineado.
        dataset_dir: Ruta absoluta del dataset de Nextclade. Por defecto, DATASET_DIR.
        reference_fasta: Ruta absoluta de la referencia propia. Su valor por defecto es None, pero debe proporcionarse porque el comando siempre la incluye.

    Returns:
        bool: True si Nextclade terminó sin errores, False si falló o si no se encontró algún archivo o el ejecutable.
    """

    # ----------------------------------------------------------------- Comando base: dataset de entrada y archivos de salida (TSV y FASTA alineado)
    cmd = ["nextclade", "run","--input-dataset", dataset_dir,"--output-tsv", output_tsv,"--output-fasta", output_fasta,]

    # ----------------------------------------------------------------- Referencia propia en lugar de la que trae el dataset
    cmd.extend(["--input-ref", reference_fasta])

    # ----------------------------------------------------------------- El FASTA con los genomas a alinear va al final, como argumento posicional
    cmd.append(input_fasta)

    # ----------------------------------------------------------------- split('/')[-1] deja solo el nombre del archivo, sin la ruta
    print(f"[ALIGN] Año {año}: {input_fasta.split('/')[-1]}")

    # ----------------------------------------------------------------- open() lanza FileNotFoundError si la ruta no existe; se cierra de inmediato porque solo se verifica
    try:
        open(input_fasta).close()
        open(reference_fasta).close()
        open(f"{dataset_dir}/pathogen.json").close() # ----------- Un dataset válido siempre trae pathogen.json; si falta, falta el dataset o su carpeta
        resultado = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as error:
        # ------------------------------------------------------------- error.filename trae la ruta (o el ejecutable nextclade) que no se encontró
        print(f"[ERROR] Año {año}: No se encontró: {error.filename}")
        return False

    if resultado.returncode == 0:
        print(f"[OK] Año {año} completado -> {output_tsv.split('/')[-1]}")
        return True
    else:
        # ------------------------------------------------------------- Solo los primeros 500 caracteres del error para no inundar la salida
        print(f"[ERROR] Año {año}: {resultado.stderr[:500]}")
        return False