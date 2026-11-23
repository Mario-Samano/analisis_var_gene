# Análisis de variantes de SARS-CoV-2 en México (2020–2024)

<!-- AYUDA: Escriban un título breve, específico y descriptivo. Puede ser provisional.
EJEMPLO: Comparación de genes de resistencia antimicrobiana en genomas de
Escherichia coli. -->

## Información general

| Dato | Información |
|:--|:--|
| Integrante 1 | Fátima Abril Gómez Martínez |
| Integrante 2 | Jana Noemí Azamar Ramírez |
| Integrante 3 | Mario Alejandro Samano Basilio |
| Fecha de creación | 25/08/2026 |
| Última actualización | 23/11/2026 |
| Repositorio | https://github.com/Mario-Samano/analisis_var_gene |

<!-- AYUDA: Mantengan actualizados el estado, la fecha y la versión. La versión debe coincidir con una etiqueta de Git cuando exista una entrega identificable. -->

## Resumen del proyecto

<!-- AYUDA: Expliquen en un párrafo el problema, su relevancia, los datos, la
solución propuesta y el resultado principal. Conviene actualizarlo al final.
EJEMPLO: Se analizarán genomas de E. coli disponibles en NCBI para identificar
y comparar genes de resistencia. Se desarrollará un flujo reproducible en Python
que obtenga los datos y genere tablas y visualizaciones comparativas. -->

*Versión preliminar*

El SARS-CoV-2 sigue mutando desde su aparición en 2019, y México fue uno de los países con más defunciones por COVID-19. Este proyecto caracteriza cómo cambió el genoma del virus en México entre 2020 y 2024. Se descargarán de NCBI las secuencias genómicas mexicanas de ese periodo mediante Biopython (`Bio.Entrez`) y se filtrarán por longitud y por contenido de bases ambiguas. Después se alinearán contra la referencia de Wuhan (NC_045512.2) con Nextclade, que asigna clados, llama mutaciones de nucleótidos y aminoácidos y evalúa la calidad de cada secuencia. Con pandas se anotarán las mutaciones por gen, se clasificarán como sinónimas o no sinónimas y se calcularán sus frecuencias por año o mes y la densidad de variación por gen. Con SciPy y Statsmodels se evaluará si los cambios de frecuencia son estadísticamente significativos, y los resultados se visualizarán con Matplotlib y Seaborn. Con `BioKEGG` se obtendrán imagenes que ayuden a explicar la vía de transmisión del virus. Todo el análisis estará en un notebook reproducible y versionado en GitHub.

## 1. Contexto y antecedentes

<!-- AYUDA: Presenten la información necesaria para comprender el proyecto.
Definan conceptos biológicos y computacionales, describan qué se conoce y citen
trabajos, datos o herramientas relacionados.
PREGUNTAS: ¿Cuál es el fenómeno de interés? ¿Qué debe conocer quien lea el
reporte? ¿Qué métodos o herramientas se han utilizado anteriormente?
EJEMPLO: La resistencia antimicrobiana es un problema de salud pública. Aunque
existen bases especializadas, comparar varios genomas requiere integrar datos
procedentes de distintos archivos. -->

El surgimiento del virus SARS-CoV-2 a finales de 2019 desencadenó la pandemia de COVID-19, que, hasta febrero de 2024, había provocado 7 millones de muertes y 770 millones de casos (Chakraborty et al., 2025). La enfermedad persiste en la actualidad y el virus continúa mutando (Cross, 2026). Sin embargo, no todos los países han reportado los mismos totales de casos y decesos, por lo que es útil estudiar la evolución del virus a escala nacional.

El SARS-CoV-2 es un virus de ARN cuyo genoma mide cerca de 30 000 pares de bases. Contiene genes que codifican proteínas estructurales, como la glicoproteína Spike (S) y la nucleocápside (N), y un extenso marco de lectura ORF1ab que da origen a proteínas no estructurales. La secuencia de referencia usada de forma estándar es la de Wuhan (NC_045512.2, Wuhan-Hu-1), derivada del primer genoma publicado del virus (Wu et al., 2020). Las diferencias de una secuencia respecto a esa referencia se describen como mutaciones, que pueden ser sustituciones, deleciones o inserciones. Las mutaciones en regiones codificantes se clasifican como **sinónimas** si no cambian el aminoácido y **no sinónimas** si lo cambian. Un ejemplo bien conocido es D614G en la proteína Spike, cuya frecuencia aumentó rápidamente durante 2020 (Korber et al., 2020).

Para comparar cientos o miles de genomas, el alineamiento por pares es poco eficiente. La vigilancia genómica del SARS-CoV-2 utiliza Nextclade, herramienta que alinea cada secuencia contra la referencia, la asigna a un clado, llama sus mutaciones y calcula métricas de control de calidad (Aksamentov et al., 2021). Por su parte, Biopython ofrece módulos para acceder a NCBI de forma programática (`Bio.Entrez`), leer formatos biológicos como FASTA y GenBank, traducir secuencias (`Bio.Seq`) y ejecutar BLAST (Cock et al., 2009). Los genomas públicos se obtienen de NCBI Nucleotide; además, existen repositorios de acceso restringido como GISAID (Elbe y Buckland-Merrett, 2017), cuyos datos no pueden redistribuirse.

## 2. Planteamiento del problema

<!-- AYUDA: Describan la dificultad, necesidad o vacío de conocimiento que
desean atender, a quién afecta y qué sucede si no se resuelve. No confundan el
problema con la herramienta ni con la solución.
EJEMPLO: La identificación manual de genes de resistencia en varios genomas es
lenta, propensa a errores y difícil de reproducir. -->

México registró alrededor de 335 000 muertes por COVID-19 entre 2020 y 2024, el quinto total más alto del mundo (Chakraborty et al., 2025). Durante ese periodo circularon distintos linajes del virus, que acumularon mutaciones. Conocer cuáles mutaciones estuvieron presentes en México, en qué genes se concentraron y cómo cambió su frecuencia a lo largo del tiempo es información necesaria para interpretar la evolución local del virus.

Responder estas preguntas con muchos genomas plantea dificultades. Descargar, filtrar, alinear y anotar las secuencias de forma manual es lento, propenso a errores y difícil de repetir. Además, un cambio observado en la frecuencia de una mutación entre dos periodos puede deberse al azar o a diferencias en el muestreo, así que debe evaluarse con pruebas estadísticas y no solo describirse.

## 3. Justificación

<!-- AYUDA: Expliquen por qué vale la pena realizar el proyecto, cuál es su
relevancia biológica, científica, técnica o social y quién podría beneficiarse.
EJEMPLO: Un flujo automatizado reducirá errores y permitirá repetir el análisis
con los mismos datos, parámetros y versiones del software. -->

Caracterizar las mutaciones del SARS-CoV-2 en México y su dinámica temporal aporta una visión local de la evolución del virus durante 2020–2024. Identificar qué genes son los más variables y qué mutaciones aumentaron o disminuyeron de manera significativa puede orientar la vigilancia genómica y el estudio de regiones del virus relevantes, como la proteína Spike.

Desde el punto de vista técnico, un flujo automatizado y documentado, que va desde la descarga de datos hasta la generación de figuras, reduce errores y permite repetir el análisis con los mismos parámetros y versiones del software. El uso de herramientas estándar (Biopython y Nextclade) facilita que otras personas reproduzcan y extiendan el trabajo con nuevos datos.

## 4. Objetivo general

<!-- AYUDA: Expresen el resultado global mediante un verbo en infinitivo. Debe
ser alcanzable durante el semestre.
EJEMPLO: Desarrollar un flujo reproducible en Python para identificar y comparar
genes de resistencia en un conjunto de genomas de E. coli. -->

Analizar mutaciones a nivel de nucleótidos y de aminoácidos presentes en genomas de SARS-CoV-2 de México de los años 2020-2024, clasificando las mutaciones entre sinónimas y no-sinónimas y calculando sus frecuencias, además de evaluar si los cambios observados a lo largo de los años son estadísticamente significativos. 

## 5. Preguntas de investigación

<!-- AYUDA: Formulen preguntas biológicas o computacionales que puedan
responderse con los datos y métodos disponibles. Indiquen qué evidencia sería
necesaria.
EJEMPLO: ¿Qué genes de resistencia aparecen en cada genoma? Evidencia: una tabla
de presencia y ausencia obtenida de las anotaciones. -->

### Pregunta 1

**Pregunta:** En los genomas de SARS-CoV-2 de México entre 2020 y 2024, ¿qué mutaciones (de nucleótidos y de aminoácidos) están presentes, en qué genes se concentran y cómo cambia su frecuencia a lo largo del tiempo?

**Evidencia necesaria:** Tabla de mutaciones por secuencia (`nextclade.tsv`) anotadas por gen y clasificadas como sinónimas o no sinónimas; tabla de frecuencias por año o mes para cada mutación de interés (por ejemplo, D614G o N501Y); y tabla de densidad de variación por gen (mutaciones observadas entre longitud del gen).

### Pregunta 2

**Pregunta:** ¿Son estadísticamente significativos los cambios en la frecuencia de las mutaciones a lo largo del tiempo?

**Evidencia necesaria:** Resultados de pruebas de Chi-cuadrado y exacta de Fisher entre periodos (2021 vs 2022) y de una prueba de tendencia temporal (regresión logística), con sus valores p.

## 6. Alcance y limitaciones

<!-- AYUDA: Delimiten organismos, muestras, datos, análisis y resultado esperado. Indiquen
qué no se abordará y las restricciones de tiempo, cómputo, acceso o calidad.
EJEMPLO: Se analizarán como máximo 20 genomas completos de RefSeq. No se
utilizarán datos clínicos ni se realizará validación experimental. -->

### Incluye

- Genomas de SARS-CoV-2 de México recolectados entre 2020 y 2024, obtenidos de NCBI Nucleotide.
- Control de calidad y filtrado de las secuencias por longitud y contenido de bases ambiguas (N).
- Alineamiento y llamado de mutaciones con Nextclade contra la referencia de Wuhan (NC_045512.2).
- Anotación de mutaciones por gen y clasificación en sinónimas y no sinónimas.
- Cálculo de frecuencias de mutaciones por periodo y de la densidad de variación por gen.
- Pruebas estadísticas de comparación entre periodos y de tendencia temporal.
- Visualización de los resultados.

### No incluye

- Secuenciación de genomas a partir de muestras de pacientes.
- Validaciones experimentales.
- Datos clínicos de los pacientes ni análisis de la severidad de la enfermedad.
- Análisis de la genética del huésped humano.
- Reconstrucción filogenética.
- Descarga masiva de genomas desde GISAID. De esa base solo se usa un genoma temprano de México, que ya está en poder del equipo.

### Limitaciones conocidas

- Las secuencias públicas de NCBI no son una muestra aleatoria de los casos: el número de genomas depositados varía entre años, regiones y laboratorios. Las frecuencias reflejan lo secuenciado, no necesariamente lo que circuló.
- Algunos registros pueden no tener fecha de recolección completa o tener metadatos faltantes, lo que reduce las secuencias utilizables para el análisis temporal.
- El genoma temprano de México proviene de GISAID, cuyos términos de uso impiden compartirlo. Esa parte del análisis no podrá reproducirse a partir del repositorio público sin acceso propio a GISAID.
- Los resultados dependen de las versiones de Nextclade y de su dataset (`nextstrain/sars-cov-2/wuhan-hu-1/orfs`), que deben registrarse.
- El análisis se limita a 2020–2024 y a una sola fuente de datos públicos.

## 7. Propuesta de solución

<!-- AYUDA: Describan el producto o estrategia que podría resolver el problema.
Es una propuesta inicial y puede cambiar. Expliquen sus componentes, no sólo las
tecnologías.
EJEMPLO: Un programa modular recibirá identificadores, descargará archivos,
extraerá genes, almacenará resultados y generará visualizaciones. -->

Se propone un pipeline modular en Python, ejecutable desde un notebook de Jupyter, con los siguientes componentes:

1. **Adquisición de datos:** un módulo que consulta NCBI Nucleotide con `Bio.Entrez` y descarga las secuencias mexicanas (2020–2024) y los metadatos asociados, además de la referencia NC_045512.2.
2. **Control de calidad:** un módulo que lee los archivos FASTA, mide la longitud de cada secuencia y descarta las incompletas o con exceso de bases ambiguas.
3. **Alineamiento y llamado de mutaciones:** una etapa que ejecuta Nextclade sobre las secuencias filtradas y genera la tabla de mutaciones y métricas de calidad.
4. **Anotación funcional:** un módulo que asigna cada mutación a su gen con las anotaciones GFF3 de la referencia y la clasifica como sinónima o no sinónima.
5. **Frecuencias y análisis temporal:** cálculo de frecuencias por periodo y de la densidad de variación por gen.
6. **Pruebas estadísticas:** comparación entre periodos y análisis de tendencia.
7. **Visualización:** generación automática de figuras y tablas.

### 7.1 Resultado o producto esperado

<!-- AYUDA: Indiquen el entregable concreto: programa, paquete, flujo de análisis,
base de datos, visualizaciones u otro producto.
EJEMPLO: Repositorio ejecutable con scripts, datos de prueba, documentación,
tabla comparativa y figuras regenerables. -->

Repositorio en GitHub con un notebook documentado y reproducible, desde la descarga de datos hasta las figuras finales; módulos en `src/`; datos de prueba pequeños; documentación; tablas de mutaciones y frecuencias; resultados de las pruebas estadísticas; y figuras regenerables (barras apiladas, líneas, heatmaps y boxplots).

## 8. Datos

### 8.1 Fuentes de datos

<!-- AYUDA: Incluyan institución, base de datos, URL, identificador, versión o
fecha de consulta y condiciones de uso. No todos los proyectos usarán NCBI.
EJEMPLO: NCBI RefSeq, GCF_000005845.2, consultado el dd/mm/aaaa. -->

| Fuente | Identificador o versión | URL | Fecha de consulta | Condiciones de uso |
|:--|:--|:--|:--|:--|
| NCBI Nucleotide | Búsqueda descrita abajo | https://www.ncbi.nlm.nih.gov/nuccore | 10/10/2026 | Datos públicos |
| NCBI RefSeq | NC_045512.2 (Wuhan-Hu-1) | https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2 | 10/10/2026 | Datos públicos |
| GISAID | Genoma temprano de México (2020); EPI_ISL_412972 | https://gisaid.org | 02/10/2026 | Acceso restringido; no se redistribuye |
| NextClade | Dataset nextstrain/sars-cov-2/wuhan-hu-1/orfs; 3.25.0 | https://docs.nextstrain.org/projects/nextclade | 15/10/2026 | Código abierto; revisar licencia |
| KEGG | KEGG PATHWAY Dataset; versión 120 | https://www.genome.jp/kegg/pathway.html | 16/11/2026 | Código abierto |


**Consulta en NCBI Nucleotide:** `"SARS-CoV-2"[Organism] AND "Mexico"[Location] AND 2020:2023[dp]`


### 8.2 Características de los datos

<!-- AYUDA: Describan organismos, muestras, variables, formatos, versiones, tamaño y otros
atributos necesarios para interpretar los datos.
EJEMPLO: Archivos FASTA y GFF3 de 20 genomas completos de E. coli. -->

- **Organismo:** SARS-CoV-2, con genoma de aproximadamente 30 kb.
- **Secuencias de México (2020–2024):** archivos FASTA o GenBank descargados de NCBI. Se desconoce aún el número de registros, que se documentará tras la descarga.
- **Metadatos:** accesión, fecha de recolección, país y otros campos de los registros, gestionados con pandas.
- **Referencia global:** secuencia NC_045512.2 de NCBI.
- **Referencia local:** un genoma temprano de México (2020) obtenido de GISAID, que ya se tiene. Es privado y no se incluye en el repositorio.
- **Anotación:** archivo GFF3 de la referencia, incluido en el dataset de Nextclade.
- **Datos derivados:** tabla `nextclade.tsv` con las mutaciones de cada genoma y sus métricas de calidad.

### 8.3 Organización de los datos

<!-- AYUDA: Muestren la estructura prevista. No suban datos sensibles, tokens,
contraseñas ni archivos grandes. Usen .gitignore y documenten cómo obtener lo
que no se guarde en Git.
EJEMPLO: data/raw conserva originales y data/processed los derivados. -->

```text
proyecto/
├── data/                            # Información usada en el proyecto
│   ├── raw/                         # Datos crudos, sin modificar
│   │   ├── ncbi_{year}.fasta/       # Secuencias y metadatos descargados con Entrez
│   │   ├── reference/               # Referencia NC_045512.2
│   │   └── gisaid_hcov.../          # Genoma temprano de México
│   ├── processed/                   # Datos derivados de notebooks como archivos .tsv
│   └── sars-cov-2/                  # Archivos de SARS-CoV-2 que necesita y descarga NextClade
├── docs/                            # Documentación del proyecto
├── notebooks/                       # Notebook de análisis reproducible
├── results/                         # Resultados
│   ├── images/                      # Imagenes (.png) generadas por los notebooks
│   └── nextclade/                   # Alineamientos globales realizados por NextClade en fasta y .tsv
├── src/                             # Código modular (funciones y clases)
├── tests/                           # Pruebas del código
├── .gitignore                       # Excluye datos grandes y datos de GISAID
├── LICENSE                          # Detalles de la licencia
├── README.md                        # Introducción y guía rápida de uso
├── CITATION.cff                     # Instrucciones para citar este repositorio
└── codemeta.json                    # Metadatos del proyecto
```

Los datos de NCBI no se guardan en Git; el notebook los descarga con la consulta indicada en 8.1. El genoma de GISAID debe obtenerse con acceso propio y colocarse en `data/raw/gisaid/`.

### 8.4 Diccionario o formato de los datos

<!-- AYUDA: Describan campos o columnas relevantes. Incluyan fragmentos pequeños
cuando ayuden a comprender el formato, pero no archivos completos.
EJEMPLO: En GFF3, seqid identifica la secuencia; type indica gene, CDS, etc. -->

**a) Metadatos y secuencias de NCBI**

| Campo | Tipo | Descripción | Valores o unidades |
|:--|:--|:--|:--|
| accession | Texto | Identificador del registro | Ejemplo: MW123456.1 |
| collection_date | Fecha | Fecha de recolección | Año, año-mes o fecha completa |
| country | Categórico | País de origen de la muestra | México |
| longitud | Numérico (calculado) | Número de bases de la secuencia | Pares de bases; umbral > 29 000 |
| proporción de N | Numérico (calculado) | Fracción de bases ambiguas | Entre 0 y 1; umbral por definir |

**b) Salida de Nextclade (nextclade.tsv)**

| Campo | Tipo | Descripción | Valores o unidades |
|:--|:--|:--|:--|
| seqName | Texto | Nombre de la secuencia | Encabezado del FASTA |
| clade | Categórico | Clado asignado | Ejemplo: 20A, 21K |
| substitutions | Texto | Mutaciones de nucleótidos | Ejemplo: A23403G |
| aaSubstitutions | Texto | Cambios de aminoácidos por gen | Ejemplo: S:D614G |
| deletions, insertions | Texto | Deleciones e inserciones | Posiciones en la referencia |
| qc.overallStatus, qc.overallScore | Categórico, numérico | Calidad de la secuencia | Nombres según la versión de Nextclade |

**c) Anotación GFF3 de la referencia**

| Campo | Tipo | Descripción | Valores o unidades |
|:--|:--|:--|:--|
| seqid | Texto | Secuencia de referencia | NC_045512.2 |
| type | Categórico | Tipo de elemento | gene, CDS, ... |
| start, end | Numérico | Posiciones del elemento | Pares de bases |
| attributes | Texto | Nombre del gen y otros datos | S, N, ORF1ab, ... |

**d) Tablas derivadas**

| Tabla | Campos | Descripción |
|:--|:--|:--|
| Frecuencias | mutación, periodo, n_con_mutación, n_total, frecuencia | Frecuencia de cada mutación por año o mes (0 a 1) |
| Densidad por gen | gen, n_mutaciones, longitud, densidad | Mutaciones observadas entre longitud del gen |


**e) Pruebas estadísticas
| Tabla | Campos | Descripción |
|:--|:--|:--|
| Chi^2 | mutation, gene, coef_year, odds_ratio, p_value, n_with_mut, n_total, test | Se evalúa la dependencia entre las mutaciones que hubo entre 2021-2022 con el p-valor |
| Prueba exacta de Fisher | mutation, gene, coef_year, odds_ratio, p_value, n_with_mut, n_total, test | Se evalúa la dependencia entre las mutaciones que hubo entre 2021-2022 con el p-valor |
| Regresión lineal | mutation, gene, coef_year, odds_ratio, p_value, n_with_mut, n_total, test | Se evalúa si existe una tendencia en los datos desde 2020-2024 |



## 9. Metodología

<!-- AYUDA: Esta sección evolucionará. Primero describan el plan y después
actualícenla con lo que realmente ejecutaron, incluidos parámetros y decisiones. -->

### 9.1 Etapas del análisis o desarrollo

<!-- AYUDA: Describan la secuencia desde la obtención de datos hasta la validación
de resultados. Relacionen cada etapa con una pregunta u objetivo.
EJEMPLO: descarga, validación, transformación, análisis, visualización y pruebas. -->

| # | Etapa | Descripción | Herramientas | Pregunta |
|:--|:--|:--|:--|:--|
| 0 | Adquisición de datos | Buscar y descargar en NCBI las secuencias de México (2020–2024) | Bio.Entrez, pandas | P1, P2 |
| 1 | Control de calidad | Descartar secuencias < 29 000 bp o con exceso de N | Biopython, pandas | P1, P2 |
| 2 | Referencias | Descargar NC_045512.2 y usar el genoma de GISAID | Bio.Entrez | P1 |
| 3 | Alineamiento global | Ejecutar nextclade run y obtener nextclade.tsv | Nextclade CLI | P1 |
| 4 | Anotación de mutaciones | Asignar mutaciones a genes (GFF3); clasificarlas como sinónimas o no sinónimas | pandas, Bio.Seq | P1 |
| 5 | Frecuencias | Frecuencia por año o mes y densidad de variación por gen | pandas | P1 |
| 6 | Pruebas estadísticas | Chi-cuadrado y Fisher entre periodos; regresión logística para análisis de tendencia | SciPy, Statsmodels | P2 |
| 7 | Visualización | Barras apiladas, líneas, heatmaps y boxplots | Matplotlib, Seaborn, BioKEGG | P1, P2 |
| 8 | Reproducibilidad | Notebook documentado y repositorio en GitHub | Jupyter, Git | Todas |


**Flujo general:** Descarga de secuencias (NCBI) → Control de calidad y filtrado → Referencias (NC_045512.2 y genoma de GISAID) → Alineamiento y llamado de mutaciones (Nextclade) → Anotación por gen y clasificación sinónima/no sinónima → Frecuencias temporales y densidad por gen → Pruebas estadísticas → Visualización → Anotación funcional.

**Pendiente:** Definir el umbral de bases ambiguas (N) para el filtrado y el uso exacto del genoma temprano de GISAID en el análisis (por ejemplo, como segunda referencia para contextualizar la evolución local).

### 9.2 Herramientas y tecnologías

<!-- AYUDA: Registren lenguajes, bibliotecas y programas con sus versiones y
propósito. No incluyan credenciales.
EJEMPLO: Python 3.x; Biopython para leer formatos biológicos; Seaborn para
visualización. -->

| Herramienta | Versión | Propósito |
|:--|:--|:--|
| Python | 3.13 | Lenguaje principal del pipeline |
| Biopython (`Bio.Entrez`, `Bio.Seq`) | Pendiente | Descargar datos de NCBI, leer FASTA/GenBank y traducir secuencias |
| pandas | Pendiente | Gestión de metadatos, lectura de `nextclade.tsv`, frecuencias y densidades |
| Nextclade CLI | 3.25.0 | Alineamiento contra la referencia, asignación de clados, llamado de mutaciones y control de calidad |
| SciPy (`scipy.stats`) | Pendiente | Pruebas de Chi-cuadrado y exacta de Fisher |
| Statsmodels | Pendiente | Regresión logística y análisis de tendencia |
| Matplotlib | Pendiente | Gráficas base |
| Seaborn | 0.13.2 | Visualización de frecuencias y densidades |
| Jupyter Notebook | Pendiente | Documentación y ejecución reproducible del análisis |
| Git y GitHub | Pendiente | Control de versiones y repositorio |
| BioKEGG   | Pendiente | Importante para la obtención de material visual para la anotación funcional |

### 9.3 Estrategia de validación

<!-- AYUDA: Expliquen cómo comprobarán código y resultados: pruebas unitarias,
datos conocidos, comparación con otra herramienta o revisión manual.
EJEMPLO: Se compararán cinco anotaciones conocidas y se probarán entradas
válidas, identificadores inexistentes y archivos incompletos. -->


- **Descarga:** comparar el número de registros que devuelve la búsqueda en Entrez con el número de secuencias descargadas, y revisar que no haya archivos truncados.
- **Filtrado:** pruebas unitarias con secuencias sintéticas de longitud y contenido de N conocidos, para comprobar que se aplican los umbrales.
- **Mutaciones:** verificar con mutaciones conocidas, por ejemplo que D614G aparezca en las secuencias del clado correspondiente, y revisar manualmente algunas secuencias en el alineamiento.
- **Clasificación sinónima/no sinónima:** probar la función con codones de resultado conocido.
- **Estadística:** Chi-cuadrado y Fisher dan resultados coherentes en tablas con conteos altos y bajos respectivamente. Regresión logística para análisis de tendencia.
- **Revisión cruzada:** toda contribución importante se revisa mediante Pull Request por otra persona del equipo.
- **Análisis de anotación funcional (opcional)**: Uso de KEGG Pathway database y discusión de los datos y su relación con la funcionalidad biológica

### 9.4 Justificación de la elección de datos y herramientas

<!-- AYUDA: Expliquen por qué eligieron cada dato, herramienta y parámetro frente a las alternativas razonables. -->

- **Datos públicos de NCBI como fuente principal.** Pueden consultarse de forma programática con `Bio.Entrez`, de modo que cualquier persona puede repetir la descarga con la misma consulta. GISAID se usa solo para el genoma temprano de México porque su acceso es restringido y sus datos no pueden redistribuirse.
- **Biopython (`Bio.Entrez`, `Bio.Seq`).** Automatiza la búsqueda y la descarga, evita pasos manuales que no quedan documentados, lee los formatos FASTA y GenBank y permite traducir codones para clasificar las mutaciones como sinónimas o no sinónimas.
- **Filtro de longitud mayor a 29 000 pb.** El genoma de referencia (NC_045512.2) mide 29 903 pb. Ese umbral descarta los genomas incompletos y tolera pérdidas pequeñas en los extremos. El filtro de bases ambiguas (N) se aplica porque las regiones sin base definida impiden llamar mutaciones de forma confiable.
- **Nextclade en lugar de un alineamiento múltiple manual.** El alineamiento por pares no escala a cientos de genomas y un alineamiento múltiple propio sería costoso de implementar y de repetir. Nextclade alinea cada secuencia de forma independiente contra una sola referencia y entrega, en una tabla, las mutaciones de nucleótidos y aminoácidos, el clado y métricas de calidad. Además es una herramienta estándar en vigilancia genómica. Su costo es que los resultados dependen de la versión del programa y del dataset, por lo que se registran.
- **Referencia NC_045512.2.** Es la referencia estándar del SARS-CoV-2, el dataset de Nextclade se construye sobre ella y facilita comparar con otros estudios, porque la nomenclatura de las mutaciones (por ejemplo, D614G) se define respecto a ella.
- **Genoma temprano de México (GISAID).** Aporta un punto de comparación local de la etapa inicial. Su uso exacto en el análisis está pendiente (ver 9.1).
- **BLAST como paso opcional.** El alineamiento global ya basta para llamar mutaciones. El local solo se agrega si se quiere estudiar con más detalle una región concreta, como el gen S, o buscar posible recombinación.
- **pandas, Jupyter, Git y GitHub.** pandas maneja las tablas de metadatos y mutaciones; el notebook documenta cada paso con sus parámetros, y Git y GitHub dan control de versiones y permiten revisar el trabajo por Pull Request.
- **Bio-Kegg** para obtener las imágenes que ejemplifican visualmente la via de infección de SARS-CoV-2 y su estructura (virión).

### 9.5 Enfoque del análisis estadístico

<!-- AYUDA: Describan qué pruebas usarán, por qué, con qué datos y cómo interpretarán los resultados. -->

**Unidad de análisis y variable.** Cada genoma es una observación. Para cada mutación de interés se registra si está presente o ausente (0/1) y el periodo de recolección. La frecuencia de un periodo es el número de genomas con la mutación entre el total de genomas de ese periodo.

**Qué mutaciones se prueban.** Se probarán las mutaciones de interés biológico y las que superen una frecuencia mínima en al menos un periodo. El valor de esa frecuencia mínima queda por definir. Los periodos con muy pocas secuencias se excluirán de las pruebas o se agruparán; el mínimo de secuencias por periodo también queda por definir.

**Pruebas según la pregunta (P2).**

| Objetivo | Prueba | Cuándo se usa |
|:--|:--|:--|
| Comparar dos periodos (2021 vs 2022) | Prueba exacta de Fisher | Opción por defecto en tablas de 2x2 |
| Comparar dos periodos (2021 vs 2022) | Chi-cuadrado | Cuando todas las frecuencias esperadas son al menos 5 y mayores |
| Tendencia a lo largo de varios periodos (2020-2024) | Regresión logística (presencia 0/1 contra tiempo) | Opción principal; da un odds ratio por unidad de tiempo |


**Justificación de la elección de las pruebas.**

- **Por qué pruebas para variables categóricas (Fisher y Chi-cuadrado).** La variable de cada genoma es binaria (mutación presente o ausente) y se compara entre dos grupos independientes (dos periodos), lo que produce una tabla de 2x2 de proporciones. Pruebas como la t de Student o el ANOVA suponen una variable continua y no aplican a este tipo de dato. Tampoco se usan pruebas de rangos como Mann-Whitney, porque no hay una variable numérica que ordenar.
- **Por qué Fisher como opción por defecto.** La prueba exacta de Fisher no depende de una aproximación y es válida con conteos pequeños. Esto importa aquí porque habrá mutaciones raras y periodos con pocas secuencias. El Chi-cuadrado es una aproximación que solo es confiable cuando las frecuencias esperadas son suficientes (al menos 5), pero es la prueba más usada para comparar proporciones. Con muestras grandes ambas dan resultados casi iguales, así que usar las dos sirve también como verificación cruzada (ver 9.3).
- **Por qué regresión logística para la tendencia.** La respuesta es binaria y el predictor es el tiempo, que es una variable ordenada. Un solo coeficiente resume la tendencia como un odds ratio por unidad de tiempo, con su intervalo de confianza y su valor p. Aprovecha todos los periodos a la vez, mientras que comparar pares de periodos obliga a elegir cuáles comparar y multiplica el número de pruebas. Además, el modelo puede ampliarse con covariables, como el clado. Se prefiere a una regresión lineal sobre las frecuencias, porque esa ignora cuántas secuencias hay en cada periodo y puede dar valores fuera de 0 a 1.
- **Limitación de ambas pruebas de tendencia.** Suponen un cambio en una sola dirección. Una mutación que aumenta y luego desaparece (por ejemplo, la de un clado que circuló unos meses) puede no mostrar tendencia significativa. Por eso estas pruebas se interpretan junto con las gráficas de línea de la etapa 8, y las comparaciones entre periodos de Fisher o Chi-cuadrado ayudan a detectar esos cambios.
- **Nivel de significancia.** Se usa un p-value = 0.05 por convención, aplicado a los valores p ajustados.

**Cómo se reportan los resultados.** Además del valor p se reportará el tamaño del efecto (diferencia de frecuencias u odds ratio). Con muchos genomas, diferencias muy pequeñas pueden resultar significativas sin importancia biológica, por lo que el valor p no se interpretará solo.

#### Checar este punto y el de arriba (mención a intervalos de confianza)
**Comparaciones múltiples.** Al probar muchas mutaciones aumenta la probabilidad de falsos positivos. Se propone corregir los valores p con el método de Benjamini-Hochberg (tasa de falsos descubrimientos, disponible en `statsmodels.stats.multitest`) y considerar significativos los valores ajustados menores a 0.05. Este criterio debe confirmarlo el equipo.

**Supuestos y cuidados.**

- Las pruebas suponen observaciones independientes, pero genomas del mismo brote o laboratorio pueden estar relacionados. Además, la muestra de NCBI no es aleatoria. Por eso los resultados describen lo secuenciado y no deben presentarse como estimaciones de la frecuencia real en la población.
- Muchas mutaciones aparecen juntas porque pertenecen al mismo clado, así que un aumento de frecuencia suele reflejar el reemplazo de un linaje y no un efecto individual de la mutación. Por ello las frecuencias también se revisarán por clado (columna `clade` de Nextclade).
- Si una mutación tiene frecuencia 0 o 1 en todo el periodo, la regresión logística no converge. Esas mutaciones se describirán sin ajustar el modelo.

## 10. Plan de trabajo

### 10.1 Distribución de responsabilidades

<!-- AYUDA: Definan responsabilidades iniciales sin aislar a cada integrante.
Toda contribución importante debe ser revisada mediante Pull Request por otra
persona.
EJEMPLO: Ana desarrolla la descarga y revisa el módulo de visualización. -->

> Estado: pendiente. El equipo definirá las responsabilidades y las revisiones por Pull Request.

### 10.2 Riesgos y alternativas

<!-- AYUDA: Identifiquen situaciones que podrían impedir o retrasar el proyecto
y definan una alternativa.
EJEMPLO: Los datos requieren demasiado almacenamiento; alternativa: reducir el
número de genomas usando criterios documentados. -->

| Riesgo | Probabilidad | Impacto | Prevención o alternativa |
|:--|:--|:--|:--|
| Pocas secuencias en algunos periodos o muestreo desigual entre años | Alta | Alto | Agrupar por año en vez de mes; reportar el número de secuencias por periodo; interpretar con cautela los periodos con pocos datos |
| Registros sin fecha de recolección completa | Media | Medio | Usar solo el año si falta el mes; excluir y documentar los registros sin fecha |
| La búsqueda en NCBI devuelve registros que no son genomas completos o no son de México | Media | Medio | Revisar los metadatos, validar la consulta y filtrar por longitud |
| El genoma de GISAID no puede compartirse y limita la reproducibilidad | Alta | Medio | Mantenerlo fuera de Git, documentar cómo obtenerlo y hacer que el pipeline funcione sin él |
| Cambios de versión de Nextclade o de su dataset alteran los resultados | Media | Medio | Registrar y fijar las versiones usadas |
| Descargas lentas o limitadas por NCBI | Media | Bajo | Descargar por lotes y guardar los datos localmente |
| Pérdida de datos o código | Baja | Alto | Usar Git y GitHub con commits frecuentes; conservar copias de los datos crudos |
| Tiempo insuficiente para el análisis opcional de BLAST | Media | Bajo | Mantenerlo como opcional y priorizar las etapas 0 a 8 |

## 11. Resultados

<!-- AYUDA: Presenten resultados vinculados con preguntas y objetivos. Incluyan
tablas o figuras con títulos, leyendas y archivos de origen. Describan aquí lo
obtenido; interprétenlo en Discusión.
EJEMPLO: Tabla de presencia y ausencia generada por src/compare_genes.py.
PRIMERA SESIÓN: dejen esta sección como pendiente. -->

## 12. Discusión

Con los datos que se obtuvieron de los alineamientos con NextClade y la posterior clasificación de las mutaciones que identificaron y mapearon, se pudo identificar que sí hay cambios de nucleótidos y de aminoácidos a lo largo de los años y que se encuentran en regiones que son de importancia funcional para SARS-CoV-2 como la proteína Spyke, N (nucleocapside), M (membrana) y ORF1a y ORF1b importantes para la sintesis de proteínas estructurales y no estrucuturales que tienen un rol para la virulencia del virus. 

Además que la clasificación de las mutaciones entre sinónimas y no sinónimas enriqueció la información al poder identificar que las mutaciones cambiaron aminoácidos que afectaron la proteína, sin embargo, por la limitación de no probar experimentalmente los resultados y conocer de esa forma los cambios en la funcionalidad que las mutaciones pudieron haber conferido, no podemos explicar cómo los cambios afectaron realmente al virus y si tuvo un papel para que la tasa de virulencia aumentara o no, pero el haber encontrado en qué parte del genoma de SARS-CoV-2 existen mayores cambios, nos da una visión de la importancia de las proteínas que estuvieron mutando y de las cuáles ya existe información en la literatura que explica su funcionalidad. 

Por otro lado, las mutaciones encontradas y su incremento en los años 2020, 2021 y 2022 coinciden con la evidencia en la literatura sobre la aparición de las cepas que se identificaron en esos años, como la transición de la variante Delta en 2021 a la variante Omicrón en 2022 (Taboada B., 2021). 

Con este trasfondo, nuestro análisis estadístico se enfocó en estos dos años y en las diez proteínas con mayor mutación que se a lo largo de los años con el fin de evaluar si los datos observados eran producto del azar o si tenían respaldo estadístico y dichas mutaciones pudieron haberse dado por presión selectiva, aunque es necesario aclarar que no podemos afirmar que haya sido presión selectiva positiva unicamente con los datos que evaluamos. 

A pesar de esta consideración, los resultados de valor p referentes a estos análisis a nivel de aminoácidos y nucleótidos sugieren que las mutaciones no fueron producto meramente del azar y que entre las mutaciones que ocurrieron entre 2020 y 2021 hay una relación que podría explicarse con una razón posiblemente biológica, aunque no podemos explicar con exactitud de qué manera y qué rol exacto tuvieron las mutaciones.

Además que, la interpretación y los resultados que se registran en este proyecto están limitados por el tamaño de la muestra (80 genomas por año), una muestra de 400 genomas no puede explicar el contexto total de la evolución del virus en México durante los años que duró la pandemia y lo que pudo significar para la salud pública en el país. 

Otro punto importante a mencionar es que las muestras fueron obtenidas al azar y no contamos con información de dónde se tomó la muestra o datos del paciente, como su edad o su sexo, para poder hacer un análisis geográfico que amplie y arroje información relacionada a dónde pudo haber existido más presencia de variantes altamente mortales y a quiénes afectaron más.

Pero aún así, con los datos arrojados de la regresión logística realizada entre las frecuencias de mutaciones en los 5 años de la pandemia, pudimos notar que sí existe una tendencia y una relación entre las mutaciones y el tiempo, aunque la tendencia no siempre fue positiva y en algunas mutaciones hubo una disminución en los años 2023 y 2024 no fue realmente grande.

Así que los resultados que este proyecto obtuvo pueden servir como un esbozo y como dirección a futuras investigaciones experimentales o bioinformáticas que busquen comprender mejor la evolución del virus.

<!-- AYUDA: Interpreten los resultados, expliquen si responden las preguntas,
compárenlos con los antecedentes y señalen limitaciones. No repitan únicamente
los valores.
EJEMPLO: La distribución observada sugiere..., aunque la interpretación está
limitada por la calidad de las anotaciones. -->


## 13. Conclusiones

<!-- AYUDA: Sinteticen qué se aprendió, qué preguntas se respondieron y si se
alcanzaron los objetivos. Incluyan aportes, limitaciones y trabajo futuro. No
introduzcan resultados nuevos.
EJEMPLO: El flujo permitió identificar..., pero será necesario incorporar... -->

El flujo que el proyecto siguió nos permitió identificar las mutaciones que ocurrieron en los genomas descargados de los diferentes años y dónde es que estas caían, logrando la identificación y caracterización de algunas de ellas a grandes rasgos y con apoyo únicamente de la literatura existente de la funcionalidad de las proteínas mutadas.

La clasificación de las mutaciones también fue crucial para poder reconocer que no solo ocurrieron mutaciones de nucleótidos que no cambiaban la cadena de aminoácidos de las proteínas, sino que sí hubieron mutaciones que las cambiaron y pudieron haber tenido cambios funcionales; los calculos de frecuencia y de densidad de mutaciones por gen arrojaron más luz a qué mutaciones y a qué proteínas afectaban, sin embargo, con solo este análisis no podemos identificar y explicar el impacto de las mutaciones a nivel funcional en el ciclo de vida y de virulencia del virus, ya que se requieren análisis experimentales para caracterizar y comprender el papel de las mutaciones que se hallaron con el análisis computacional.

Aún con estas limitaciones, este proyecto logró sus objetivos al poder identificar las frecuencias y densidades de mutaciones a lo largo del tiempo, identificar las regiones en el genoma en que estas caían y comprobar su significancia estadística, pero para enriquecer y ampliar la información a la vez que construir un panorama más amplio y completo, es necesario incorporar más genomas para agrandar la muestra y añadir verificaciones experimentales para caracterizar el cambio de funcionalidad que confirieron las mutaciones.


## 14. Disponibilidad, licencia y citación

<!-- AYUDA: Indiquen dónde está el código, bajo qué licencia puede reutilizarse
y cómo citarlo. Relacionen esta sección con LICENSE, CITATION.cff, codemeta.json,
release final y, cuando corresponda, un DOI.
EJEMPLO: Código en GitHub bajo MIT; cita disponible en CITATION.cff. -->

**Código:** Almacenado en GitHub (https://github.com/Mario-Samano/analisis_var_gene)  
**Datos:** Las secuencias de NCBI pueden reobtenerse con la consulta indicada en 8.1. El genoma de GISAID no se distribuye por sus términos de uso; pero puede acceder a él si cuenta con un usuario de **GISAID** o descargando el archivo fasta en presente en este repositorio en `data/raw`.  
**Licencia del código:** [MIT License](https://github.com/Mario-Samano/analisis_var_gene/blob/main/LICENSE)  
**Cómo citar:** [CITATION.cff](https://github.com/Mario-Samano/analisis_var_gene/blob/main/CITATION.cff)
**Versión o release:** *Pendiente*

## 15. Referencias

<!-- AYUDA: Registren publicaciones, datos, software y documentos consultados en
un formato uniforme. Incluyan DOI, URL o identificadores persistentes. Toda cita
del texto debe aparecer aquí.
EJEMPLO: Blattner, F. R. et al. (1997). The complete genome sequence of
Escherichia coli K-12. Science, 277(5331), 1453–1462.
https://doi.org/10.1126/science.277.5331.1453 -->

<!-- Nota para el equipo: verifiquen volumen, páginas y DOI de las referencias 2, 3, 5 y 6 antes de entregar. -->

1. Aksamentov, I., Roemer, C., Hodcroft, E.B., Neher, R.A. (2021). Nextclade: clade assignment, mutation calling and quality control for viral genomes. *Journal of Open Source Software, 6*(67), 3773. https://doi.org/10.21105/joss.03773

2. Chakraborty, C., Bhattacharya, M., Chatterjee, S., Lee, S.S., Bhattacharya, P., Ohimain, E.I., Wen, Z. Das, A., Rai, A., Abdelhameed, A.S., Agoramoorthy, G., Zayed, H., Byrareddy, S.N. (2025). Comprehensive global-scale evaluation of the COVID-19 pandemic associated with 234 countries, territories, and sub-national locations during 2020–2024. *Folia Microbiologica*. https://doi.org/10.1007/s12223-025-01299-9

3. Cock, P.J.A., Antao, T., Chang, J.T., Chapman, B.A., Cox, C.J., Dalke, A., Friedberg, I., Hamelryck, T., Kauff, F., Wilczynski, B., de Hoon, M.J.L. (2009). Biopython: freely available Python tools for computational molecular biology and bioinformatics. *Bioinformatics, 25*(11), 1422–1423. https://doi.org/10.1093/bioinformatics/btp163

4. Cross, G. (2026, 11 de marzo). *6 years since COVID-19 pandemic began. What happened March 11, 2020* [sic]. USA Today. https://www.usatoday.com/story/news/nation/2026/03/11/covid-19-pandemic-march-11-2020/89082810007/

5. Elbe, S., Buckland-Merrett, G. (2017). Data, disease and diplomacy: GISAID's innovative contribution to global health. *Global Challenges, 1*(1), 33–46. https://doi.org/10.1002/gch2.1018

6. Korber, B., Fischer, W.M., Gnanakaran, S., Yoon, H., Theiler, J., Abfalterer, W., et al. (2020). Tracking changes in SARS-CoV-2 Spike: evidence that D614G increases infectivity of the COVID-19 virus. *Cell, 182*(4), 812–827. https://doi.org/10.1016/j.cell.2020.06.043

7. Wu, F., Zhao, S., Yu, B., Chen, Y.-M., Wang, W., Song, Z.-G., et al. (2020). A new coronavirus associated with human respiratory disease in China. *Nature, 579*, 265–269. https://doi.org/10.1038/s41586-020-2008-3

8. Taboada B, Zárate S, Iša P, Boukadida C, Vazquez-Perez JA, Muñoz-Medina JE, Ramírez-González JE, Comas-García A, Grajales-Muñiz C, Rincón-Rubio A, Matías-Florentino M, Sanchez-Flores A, Mendieta-Condado E, Verleyen J, Barrera-Badillo G, Hernández-Rivas L, Mejía-Nepomuceno F, Martínez-Orozco JA, Becerril-Vargas E, López S, López-Martínez I, Ávila-Ríos S, Arias CF. Genetic Analysis of SARS-CoV-2 Variants in Mexico during the First Year of the COVID-19 Pandemic. Viruses. 2021 Oct 26;13(11):2161. doi: 10.3390/v13112161. PMID: 34834967; PMCID: PMC8622467. 

---

<!-- ORIENTACIÓN PARA LAS DOS PRIMERAS SESIONES:
Completen Información general, Resumen provisional, secciones 1 a 7, fuentes de
datos preliminares y plan de trabajo. Metodología, Resultados, Discusión,
Conclusiones Y Disponibilidad evolucionarán durante el
semestre. Sustituyan las indicaciones entre corchetes por contenido del equipo. -->
