# Búsqueda de variantes clínicas perjudiciales, benéficas y similares a esos grupos asociadas con el desarrollo de COVID-19 severo entre mexicanos

_Versión preliminar_. 
Se buscarán variantes genéticas que inciden en la susceptibilidad de la enfermedad por SARS-CoV-2 (COVID-19) en genomas de mexicanos residentes en Estados Unidos.

Para conocer el planteamiento, las preguntas de investigación, la metodología y
los resultados, consulta el [reporte-proyecto.md](https://github.com/Mario-Samano/analisis_var_gene/blob/main/docs/reporte-proyecto.md).



## Funcionalidades
#### _Pendientes, se agregarán mediante el desarrollo del proyecto:_

- [Funcionalidad disponible 1]
- [Funcionalidad disponible 2]
- [Funcionalidad disponible 3]

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
├── notebooks/  # Carpeta para organizar mejor el código generado.
├── results/   # Se guardarán aquí posteriormente los resultados obtenidos
├── src/   # Carpeta que contiene el código que se desarrollará 
└── tests/   # Resultados de pruebas realizadas a lo largo del proyecto
├── LICENSE    # Detalles de la licencia
└── README.md    # Introducción y guía rápida de uso
```


## Requisitos
#### Pendiente algunos detalles de la siguiente información:
- Python [versión] 
- Librerias: 
| Herramienta | Versión |
|:--|:--|
| Processes (librería de Python) | 3.14.7 |
| Seaborn (librería de Python) | 0.13.2 |

- [Recurso computacional o condición de acceso]


## Datos
### _Pendientes, se agregarán mediante el desarrollo del proyecto:_

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

La procedencia y características detalladas se describen en el
[reporte del proyecto](docs/reporte-proyecto.md).

## Uso

[Expliquen qué hace el siguiente comando y qué entradas necesita.]

```bash
python src/main.py [argumentos]
```

[Indiquen dónde se guardan los resultados.]

<!--
AYUDA:
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
python scripts/download_data.py
python src/run_analysis.py
python src/create_figures.py
```

Los resultados esperados se generarán en `results/`.

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
- Fátima Abril Gómez Martínez — [Contribución o responsabilidad general]
- Mario Alejandro Samano — [Contribución o responsabilidad general]
- Jana Noemí Azamar Ramírez — [Contribución o responsabilidad general]

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

