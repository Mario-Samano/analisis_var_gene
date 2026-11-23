# Análisis de variantes de SARS-CoV-2 en México (2020–2024)

_Versión preliminar_. 
Se buscarán variantes genéticas en genomas de SARS-CoV-2 (COVID-19) en regiones de genes potenciales a incidecia en la susceptibilidad de la enfermedad con el mismo nombre en pacientes mexicanos

Para conocer el planteamiento, las preguntas de investigación, la metodología y
los resultados, consulta el [reporte-proyecto.md](https://github.com/Mario-Samano/analisis_var_gene/blob/main/docs/reporte-proyecto.md).


## Funcionalidades

- Descarga de genomas mediante identificadores de NCBI de los años 2020-2024 especificamente
- Alineamiento de genomas con la herramienta NextClade contra un genoma de referencia
- Mapeo de las regiones de los genomas en donde se encuentran mutaciones a nivel de aminoácidos y nucleótidos 
- Evaluación de frecuencias y de densidades de mutaciones por gen a nivel de aminoácidos y nucleótidos en los genomas de los años 2020-2024
- Análisis estadísticos de las tablas de mutaciones generadas para conocer la signifcancia de los datos
- Obtención de imágenes desde KEGG para ilustrar la anotación funcional del virus SARS-CoV-2


<!--
AYUDA:
Describan solamente capacidades que ya funcionan. Comiencen cada elemento con un
verbo. Las funciones planeadas deben registrarse como issues y/o en GitHub Projects.

EJEMPLO:
- Descarga genomas mediante identificadores de NCBI.
- Lee archivos FASTA y GFF3.
- Genera una tabla de presencia y ausencia de genes.
-->

## Estructura del repositorio

```text
proyecto/
├── data/   #Información importante usada en el proyecto
│   ├── raw/   # Carpeta de datos crudos
│   └── processed/   # Carpeta de datos de interés
├── docs/   # Carpeta que contiene la documentación del proyecto
├── notebooks/  # Carpeta que contiene y organiza los códigos generados dependiendo de su función
├── results/   # Se guardarán aquí posteriormente los resultados obtenidos
├── src/   # Carpeta que contiene el código que se desarrollará 
└── tests/   # Resultados de pruebas realizadas a lo largo del proyecto
├── LICENSE    # Detalles de la licencia
├── README.md    # Introducción y guía rápida de uso
├── CITATION.cff  # Archivo con instrucciones para citar este repositorio
└── codemeta.json  # Archivo con los metadatos del proyecto
```


## Requisitos
#### Pendiente algunos detalles de la siguiente información:

- Python 3.13 
- Nextclade 3.25.0
- Librerias: 

| Herramienta | Descripción breve de uso                                                                                                                                       | Versión   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| BioPython   | Uso de: Bio.Entrez para descarga de genomas de NCBI  Bio.Seq para manipular los genomas obtenidos de NCBI y GISAID | 1.88 |
| pandas      | En general su uso se hace para manipular con los datos estructurados de los datos obtenidos                                                                    | 2.2.3 |
| Nextclade   | Uso de Nexclade para el alineamiento global de genomas con el de Referencia (Wuhan-Hu-1)                                                                      | 3.25.0 |
| SciPy       | Se usa esta libreria para las pruebas estadisticas                                                                                                             | 1.15.2 |
| Statsmodels | Se usa para regresión lineal y análisis de tendencia                                                                                                           | 2.2.5 |
| Matplotlib  | Su uso recae en volver en difentes formatos gráficos los resultados obtenidos de las pruebas estádisticas                                                      | 3.11.2 |
| Seaborn     | Importante para la visualización de frecuencias y de densidades                                                                                                | 0.11.1 |
| BioKEGG     | Importante para la obtención de material visual para la anotación funcional                                                                                    | 1.88 |

- [Recurso computacional o condición de acceso]


## Datos
<!--

[Expliquen cómo obtener los datos y dónde colocarlos.]

AYUDA:
Indiquen la fuente, el comando o enlace de descarga y la carpeta de destino. No
repitan aquí la descripción completa de muestras, formatos, variables o criterios
de selección; enlacen el reporte. Si los datos no pueden publicarse, expliquen los
requisitos y el procedimiento autorizado para acceder a ellos.

EJEMPLO:
Los datos proceden de NCBI RefSeq. Para descargarlos, ejecuta:

    python scripts/download_data.py

Los archivos se guardarán en data/raw/. Los identificadores, versiones y criterios
de selección se documentan en docs/reporte-proyecto.md.
-->

Los datos de los 80 genomas por año proceden de **NCBI Nucleotide** y **NCBI RefSeq***, incluyendo el genoma de referencia global con ID: NC_045512.2 (Wuhan-Hu-1) 
Para su descarga, ejecute:

    python notebooks/download_genomes.ipynb

Los datos del genoma de referencia mexicano se obtuvieron de **GISAID** con el ID: EPI_ISL_412972.
Si cuenta con un usuario en dicha plataforma, puede descargarlo con su ID directamente, de otra manera, puede acceder a él en la carpeta de data de este repositorio.

Los resultados los encontrará con el nombre de "wuhan_ref.fasta" y como "gisaid_hcov-19_2026_10_02_20.fasta" en la carpeta `raw` en `data`:

```text
proyecto/
├── data/   #Datos esenciales para el proyecto
│   ├── raw/ # Datos crudos, como genomas de referencia y el genoma mexicano
|       ├──reference # Aquí se encuentra el genoma Wuhan-Hu-1 
``` 

La procedencia y características detalladas se describen en el
[reporte del proyecto](docs/reporte-proyecto.md).


## Uso

[Expliquen qué hace el siguiente comando y qué entradas necesita.]

Para descargas los datos y ver sus outputs, ejecute:
```bash
    python notebooks/download_genomes.ipynb 
```

El comando generará en `/data/raw/`:
- ncbi_{year}.fasta (2020-2024)
- reference/wuhan_ref.fasta

Y en "data/processed/":
- boxplots_scatterplots_generales.png
- tendencias_genomas_longitud.png


Para realizar los alineamientos de los genomas con NextClade, ejecute:
```bash
    python notebooks/nextclade_alignment.ipynb
```
El comando generará 11 archivos fasta en `/results/nextclade/` con los nombres: 
- alineamiento.{year}.fasta (year= 2020-2024)
- nextclade_{year}.tsv (year= 2020-2024)
- input_2020_con_mexicano.fasta
Además que con un subproceso usando `run_nexclade.py` se bajará la base de datos de NextClade correspondiente a SARS-CoV-2, esta carpeta está en `data`, llamada `sars-cov-2` y contiene 7 archivos:
- reference.fasta
- sequences.fasta
- genome_annotation.gff3


Para obtener los resultados de las frecuencias de mutación, su clasificación de si son sinónimas o no y el porcentaje de densidad de mutaciones encontradas por NextClade, ejecute:
```bash
    python notebooks/calculating_density_frequencies.ipynb
```
El comando generará 5 archivos .tsv en `/data/processed/`  llamados: 
- nueva_densidad_por_gen.tsv
- nuevas_frecuencias_aa_por_anio.tsv 
- nuevas_frecuencias_nt_por_anio.tsv 
- nuevas_mutaciones_clasificadas.tsv
- nuevo_resumen_por_gen.tsv

Y cinco archivos .png en `/results/images/` llamados:
- densidad_por_gen.png 
- top10_nt_comunes.png  
- top10_aa_comunes.png 
- aa_cambio_por_ola.png
- heatmap_mutaciones_por_gen.png


Para obtener la significancia de los datos generados por `calculating_density_frequencies.ipynb` y evaluarlos con pruebas Chi^2, Fisher y Regresión logística, ejecute:

```bash
    python notebooks/pruebas_estadisticas.ipynb
```
El comando generará dos archivos .tsv en `/data/processed/`
- resultados_estadisticos_aa.tsv
- resultados_estadisticos_nt.tsv 

Y seis archivos .png en `/results/images/` llamados:
- slope_aa.png  
- slope_nt.png 
- heatmap_frecuencias_aa.png 
- heatmap_frecuencias_nt.png
- frecuencias_mutaciones_aa.png  
- frecuencias_mutaciones_nt.png


Para obtener desde KEGG (Kyoto Encyclopedia of Genes and Genomes)información relacionada a la anotación funcional de SARS-CoV-2 obten

```bash
    python notebooks/mapping_mutations_to_kegg.ipynb
```
El comando bajará 2 archivos .png en `/results/images/` llamados:
- ko05171_mutaciones_por_cambio.png
- map03262_covid_virion.png

<!--
AYUDA:

[Indiquen dónde se guardan los resultados.]


Incluyan al menos un ejemplo mínimo que pueda copiarse y ejecutarse. Sustituyan
los corchetes por valores reales. Expliquen entradas, opciones importantes y
archivos de salida sin describir toda la metodología.

EJEMPLO:
Para analizar los identificadores incluidos en data/accessions.txt:

    python src/main.py --input data/accessions.txt --output results/

El comando generará results/gene_matrix.csv y results/heatmap.png.
-->

## Reproducción de resultados

Ejecuten los siguientes pasos en el orden indicado:

```bash
python notebooks/download_genomes.ipynb
python notebooks/nextclade_alignment.ipynb
python notebooks/calculating_density_frequencies.ipynb
python notebooks/pruebas_estadisticas.ipynb
python mapping_mutation_to_kegg.ipynb

```

Los resultados esperados se guardarán en `/data` en raw y processed. Además de que después de ejecutar todos los comandos, los demás resultados estarán en `/results/images` y `/results/nextclade`, en la sección anterior (Uso) se dan más detalles de los archivos generados esperados.

<!--
AYUDA:
Proporcionen la ruta más corta para regenerar el resultado principal desde los
datos originales. Los comandos deben indicar el orden correcto. Si el proceso
requiere parámetros o archivos de configuración, indíquenlos.
Las explicaciones científicas e interpretación de resultados pertenecen al reporte.

EJEMPLO:
Después de ejecutar los tres comandos se crearán la tabla comparativa y las
figuras utilizadas en el reporte. Sus nombres esperados deben indicarse aquí.
-->


## Documentación

- [Reporte del proyecto]([docs/reporte-proyecto.md](https://github.com/Mario-Samano/analisis_var_gene/blob/main/docs/reporte-proyecto.md)): contiene el problema, las preguntas, la metodología y los resultados obtenidos.
- [CITATION]([CITATION.cff](https://github.com/Mario-Samano/analisis_var_gene/tree/main/results/images)): contiene la información para citar este proyeecto.
- codemeta.json ([codemeta.json](**_agregar_**)): archivo con la metadadta del proyecto.
- [LICENSE](https://github.com/Mario-Samano/analisis_var_gene/blob/main/LICENSE): Licencia utilizada en el proyecto. 

<!--
AYUDA:
Incluyan únicamente documentos que existan y comprueben sus enlaces. Agreguen
otros documentos sólo si evitan que el README sea demasiado extenso.

EJEMPLO:
- El reporte contiene el problema, las preguntas, la metodología y los resultados.
-->

## Equipo

#### Pendiente detalles de la siguiente información:
- Fátima Abril Gómez Martínez — Descarga de datos, visualización, análisis de frecuencias, análisis de datos de anotación funcional.
- Mario Alejandro Samano Basilio — Descarga de datos, visualización, alineamientos globales, análisis de frecuencias y estadísticos.
- Jana Noemí Azamar Ramírez — Documentación, análisis de datos de anotación funcional y estadísticos.

<!--
AYUDA:
Identifiquen a las tres personas. Describan brevemente sus contribuciones generales.
Las actividades específicas y revisiones se consultan en los issues, Pull Requests,
GitHub Projects y el historial de Git.

EJEMPLO:
- Ana Pérez — procesamiento de datos y pruebas.
- Luis López — análisis y visualización.
- María García — documentación e integración.
-->

## Citación

Si utilizas este software, consulta [CITATION.cff](https://github.com/Mario-Samano/analisis_var_gene/tree/main/results/images) o la opción
**Cite this repository** de GitHub.

<!--
AYUDA:
Mantengan CITATION.cff actualizado con autores, título y versión. Si el proyecto
obtiene un DOI, añadan aquí la referencia recomendada.

EJEMPLO:
La forma recomendada de citar la versión v1.0.0 se encuentra en CITATION.cff.
-->

## Licencia

Licencia bajo la que trabajaremos es la licencia MIT. Consulta [LICENSE](https://github.com/Mario-Samano/analisis_var_gene/blob/main/LICENSE) para conocer
los términos de uso.


## Agradecimientos
#### Pendiente la siguiente información:

[Incluyan reconocimientos institucionales o académicos]

<!--
AYUDA:
Esta sección es opcional. Reconozcan laboratorios, docentes, instituciones,
proyectos o financiamientos que apoyaron el trabajo. No incluyan como autores a
personas que sólo deban aparecer en los agradecimientos.

EJEMPLO:
Proyecto desarrollado en la Licenciatura en Ciencias Genómicas, UNAM, como parte
de la asignatura [nombre].
-->

---

