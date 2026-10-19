# Análisis de variantes del SARS-CoV-2 en México (2020–2024)

_Versión preliminar_. 
Se buscarán variantes genéticas en genomas de SARS-CoV-2 (COVID-19) en regiones de genes potenciales a incidecia en la susceptibilidad de la enfermedad con el mismo nombre en pacientes mexicanos

Para conocer el planteamiento, las preguntas de investigación, la metodología y
los resultados, consulta el [reporte-proyecto.md](https://github.com/Mario-Samano/analisis_var_gene/blob/main/docs/reporte-proyecto.md).



## Funcionalidades
#### _Pendientes, se agregarán más mediante el desarrollo del proyecto:_

- Descarga de genomas mediante identificadores de NCBI de los años 2020-2024 especificamente


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
└── README.md    # Introducción y guía rápida de uso
```


## Requisitos
#### Pendiente algunos detalles de la siguiente información:

- Python 3.13 
- Librerias: 

| Herramienta | Descripción breve de uso                                                                                                                                       | Versión   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| BioPython   | Uso de: Bio.Entrez para descarga de genomas de NCBI  Bio.Seq para manipular los genomas obtenidos de NCBI y GISAID Bio.Blast para poder usar el programa BLAST | Pendiente |
| pandas      | En general su uso se hace para manipular con los datos estructurados de los datos obtenidos                                                                    | Pendiente |
| Nexclade    | Uso de Nexclade para el alineamiento global de genomas con el de Referencia (Wuhan-Hu-1)                                                                       | Pendiente |
| BLAST+      | Uso de BLAST para el alineamiento local de genomas con el de Referencia (Mexicano)                                                                             | Pendiente |
| SciPy       | Se usa esta libreria para las pruebas estadisticas                                                                                                             | Pendiente |
| Statsmodels | Se usa para regresión lineal y análisis de tendencia                                                                                                           | Pendiente |
| Matplotlib  | Su uso recae en volver en difentes formatos gráficos los resultados obtenidos de las pruebas estádisticas                                                      | Pendiente |
| Seaborn     | Importante para la visualización de frecuencias y de densidades                                                                                                | Pendiente |

- [Recurso computacional o condición de acceso]


## Datos

[Expliquen cómo obtener los datos y dónde colocarlos.]

<!--
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

Los datos de genomas proceden de **NCBI Nucleotide** y **NCBI RefSeq***, incluyendo el genoma de referencia global con ID: NC_045512.2 (Wuhan-Hu-1) 
Para su descarga, ejecute:

    python notebooks/download_genomes.ipynb

Los resultados los encontrará con el nombre de "wuhan_ref.fasta" en la carpeta raw en data:
```text
proyecto/
├── data/   #Datos esenciales para el proyecto
│   ├── raw/ # datos crudos, como genomas de referencia
|       ├──reference #aquí se encuentra el genoma Wuhan-Hu-1 
``` 

El genoma de referencia local del paciente cero en México procede de **GISAID** (hCoV-19). Para su obtención, descargue el archivo "gisaid_hcov-19_2026_10_02_20.fasta" de la carpeta raw en data:

```text
proyecto/
├── data/   #Información importante usada en el proyecto
│   ├── raw/ # aquí se encuentra el archivo con el genoma de SARS-CoV-2 del paciente 0 en México
```
O si cuenta con un usuario en GISAID, puede buscarlo con el siguiente ID:
ID: EPI_ISL_412972

La procedencia y características detalladas se describen en el
[reporte del proyecto](docs/reporte-proyecto.md).


## Uso

[Expliquen qué hace el siguiente comando y qué entradas necesita.]

Para descargas los datos y ver sus outputs, ejecute:
```bash
    python notebooks/download_genomes.ipynb 
```

El comando generará "/data/raw/ncbi_{year}.fasta", "/data/raw/reference/wuhan_ref.fasta", "data/processed/boxplots_scatterplots_generales.png" y "data/processed/tendencias_genomas_longitud.png"



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
_parte pendiente, se irá actualizando conforme el proyecto avance_

```bash
python notebooks/download_genomes.ipynb

```

Los resultados esperados se guardarán en `data` en 'raw y processed.

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

- [Reporte del proyecto]([docs/reporte-proyecto.md](https://github.com/Mario-Samano/analisis_var_gene/blob/main/docs/reporte-proyecto.md))


<!--
AYUDA:
Incluyan únicamente documentos que existan y comprueben sus enlaces. Agreguen
otros documentos sólo si evitan que el README sea demasiado extenso.

EJEMPLO:
- El reporte contiene el problema, las preguntas, la metodología y los resultados.
-->

## Equipo

#### Pendiente detalles de la siguiente información:
- Fátima Abril Gómez Martínez — Descarga de datos y pruebas
- Mario Alejandro Samano — Descarga de datos y alineamientos globales
- Jana Noemí Azamar Ramírez — Documentación 

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

Si utilizas este software, consulta [CITATION.cff](CITATION.cff) o la opción
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

