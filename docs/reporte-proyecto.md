# Búsqueda de variantes clínicas perjudiciales, benéficas y similares a esos grupos asociadas con el desarrollo de COVID-19 severo entre mexicanos

<!-- AYUDA: Escriban un título breve, específico y descriptivo. Puede ser provisional.
EJEMPLO: Comparación de genes de resistencia antimicrobiana en genomas de
Escherichia coli. -->

## Información general

| Dato | Información |
|:--|:--|
| Integrante 1 | Mario Alejandro Samano Basilio |
| Integrante 2 | Jana Noemí Azamar Ramírez |
| Integrante 3 | Fátima Abril Gómez Martínez |
| Fecha de creación | 25/08/2026 |
| Última actualización | 01/09/2026 |
| Repositorio | https://github.com/Mario-Samano/analisis_var_gene |

<!-- AYUDA: Mantengan actualizados el estado, la fecha y la versión. La versión debe coincidir con una etiqueta de Git cuando exista una entrega identificable. -->

## Resumen del proyecto

<!-- AYUDA: Expliquen en un párrafo el problema, su relevancia, los datos, la
solución propuesta y el resultado principal. Conviene actualizarlo al final.
EJEMPLO: Se analizarán genomas de E. coli disponibles en NCBI para identificar
y comparar genes de resistencia. Se desarrollará un flujo reproducible en Python
que obtenga los datos y genere tablas y visualizaciones comparativas. -->

[Redacten aquí el resumen.]

*Versión preliminar*
Se investigará si en los genomas mexicanos hay variantes genéticas que inciden en la susceptibilidad a desarrollar síntomas severos de COVID-19, una enfermedad que afectó de manera desproporcional a los mexicanos y centroamericanos que residían en Estados Unidos de América. Las variantes se tomarán de ClinVar y, mediante herramientas de Bash que serán parte de un flujo estructurado en Python, serán buscadas en genomas de migrantes con ancestría mexicana. Al final, se usará Python y Seaborn para calcular y graficar las frecuencias de las variantes mencionadas.

## 1. Contexto y antecedentes

<!-- AYUDA: Presenten la información necesaria para comprender el proyecto.
Definan conceptos biológicos y computacionales, describan qué se conoce y citen
trabajos, datos o herramientas relacionados.
PREGUNTAS: ¿Cuál es el fenómeno de interés? ¿Qué debe conocer quien lea el
reporte? ¿Qué métodos o herramientas se han utilizado anteriormente?
EJEMPLO: La resistencia antimicrobiana es un problema de salud pública. Aunque
existen bases especializadas, comparar varios genomas requiere integrar datos
procedentes de distintos archivos. -->


El surgimiento del virus SARS-CoV-2 a finales de 2019 desencadenó la catastrófica pandemia de COVID-19, que, hasta febrero de 2024, había provocado 7 millones de muertes y 0.77 billones de casos (Chakraborty et al., 2025). Esta enfermedad persiste en la actualidad y SARS-CoV-2 continúa mutando (Cross, 2026); sin embargo, no todos los países han reportado los mismos totales de casos y decesos, ni todos los grupos poblacionales han tenido riesgos similares de contraer la afección y que esta se agrave (Gong et al., 2024; Riley et al., 2025).

Al principio, fue evidente que los pacientes más propensos a enfermar de gravedad, e incluso perecer, tras ser infectados por el virus eran los adultos mayores, las personas con inmunosupresión, y los individuos que padecían enfermedades crónicas (Montero et al., 2025). Dado que la principal vía de transmisión del COVID-19 es la exposición a gotículas o aerosoles dejados en el ambiente si una persona infectada respira, estornuda o tose, se halló que estos factores multiplicaban el riesgo de contraer la enfermedad y que ella se agravara: residir en ciudades con alta densidad poblacional; tener un trabajo que no podía efectuarse de manera remota, y que soliera involucrar tener contacto recurrente con gente; carecer de acceso a servicios de salud y un suministro estable de agua para lavarse las manos; entre otros (Giné-Garriga et al., 2021; Gong et al., 2024).

No obstante, con el paso del tiempo se empezaron a desarrollar estudios sobre los factores de riesgo genéticos vinculados con el COVID-19. Así, se descubrió que la ancestría y las variantes genéticas presentes en una población (por ejemplo, los polimorfismos de un solo nucleótido, deleciones e inserciones), podían incidir en diversos aspectos de la dolencia: la susceptibilidad a ser infectado por el virus causante, el curso clínico y el desenlace (Shikov et al., 2020., Secolin et al., 2021; Fabrizio et al., 2022; Montero et al., 2025., Rocha et al., 2025). 

Cabe destacar que la principal metodología de estas investigaciones ha sido extraer muestras sanguíneas de pacientes que tenían la enfermedad, o incluso desarrollaron síntomas graves y fueron admitidos a unidades de cuidados intensivos, secuenciar sus genomas e identificar frecuencias alélicas y genotípicas de un conjunto de genes preseleccionados con base en su relevancia fisiopatológica para la progresión del COVID-19 (Montero et al., 2025; Rocha et al., 2025). Otros trabajos omitieron los dos primeros pasos porque utilizaron masivas bases de datos donde se resguardaban genomas o exomas secuenciados (Shikov et al., 2020; Secolin et al., 2021; Fabrizio et al., 2022).
 
<br>

## 2. Planteamiento del problema

<!-- AYUDA: Describan la dificultad, necesidad o vacío de conocimiento que
desean atender, a quién afecta y qué sucede si no se resuelve. No confundan el
problema con la herramienta ni con la solución.
EJEMPLO: La identificación manual de genes de resistencia en varios genomas es
lenta, propensa a errores y difícil de reproducir. -->

Los estudios encaminados a dilucidar la presencia de variantes genéticas que inciden en la predisposición a contraer COVID-19 y la severidad de los síntomas se han centrado en poblaciones de Europa del Sur (Shikov et al., 2020), Brazil (Secolin et al., 2021; Rocha et al., 2025), y de origen asiático, africano o europeo (Fabrizio et al., 2022). El único estudio enfocado en mexicanos se realizó entre 2020 y 2021; asimismo, solo se buscaron variantes en 6 genes que en ese momento se sabía que estaban vinculados con los mecanismos moleculares de la enfermedad (Montero et al., 2025). 

La escasa información sobre la existencia de variantes genéticas entre los mexicanos vinculadas con la infección y el progreso clínico de COVID-19 es inquietante, ya que en 2023 México estaba en el doceavo puesto de casos reportados de COVID-19 (Montero et al., 2025). También se estima que, entre 2020 y 2024, la dolencia provocó alrededor de 335 000 óbitos en ese territorio; este fue el quinto total más elevado en el mundo (Chakraborty et al., 2025). 

Por añadidura, Riley et al. (2025) aseveran que, al calcular la mortalidad excesiva de COVID-19, que es la diferencia entre los fallecimientos registrados y las muertes predichas de manera estadística dadas las tendencias epidemiológicas, se constató que los mexicanos y centroamericanos que radican en California, Estados Unidos de América (EUA), fueron un grupo afectado de forma notoria. Ellos presentan algunos de los factores de riesgo enumerados más arriba: tienen edades avanzadas, enfrentan barreras para acceder a servicios de salud, y sus ocupaciones conllevan interacción regular con otras personas. Además, es común que su nivel educativo y su lugar de procedencia los orillen a tomar vacantes laborales precarias y que no los protejan de exponerse al virus causante de la susosidicha patología (Riley et al., 2025). 

<br>

## 3. Justificación

<!-- AYUDA: Expliquen por qué vale la pena realizar el proyecto, cuál es su
relevancia biológica, científica, técnica o social y quién podría beneficiarse.
EJEMPLO: Un flujo automatizado reducirá errores y permitirá repetir el análisis
con los mismos datos, parámetros y versiones del software. -->

Realizar un estudio orientado a la detección, en genomas mexicanos, de variantes genéticas que repercuten en la predisposición a exhibir síntomas severos de COVID-19 permitiría enriquecer y actualizar el análisis realizado por Montero et al. (2025). En particular, focalizar el trabajo en personas oriundas de México pero que se encuentran en Los Ángeles (L.A.), California brindaría información genética sobre una comunidad abundante en L.A. (Riley et al., 2025) y que fue perjudicada por una significativa mortalidad excesiva de la antedicha enfermedad debido a numerosas disparidades socioeconómicas; aunado a ello, indicaría si entre la población había genotipos que ahora se sabe que influyen en la susceptibilidad de que un paciente infectado por SARS-CoV-2 llegue al estado crítico.

Si esta investigación logra esclarecer cuán frecuentes son las variantes que auspician o minimizan el riesgo de tener COVID-19 severo, estos hallazgos podrían servir para diseñar mejores estrategias de salud pública en EUA. Esas iniciativas podrían más adelante modificarse para su implementación en México, luego de contrastar los resultados del presente proyecto con análisis llevados a cabo empleando datos del Biobanco Mexicano u otro repositorio con información específica sobre personas que nacieron y viven en México.

Al mismo tiempo, si en esta investigación se detecta que los mexicanos en EUA poseen variantes genéticas (beneficiosas, patogénicas o afines a esas categorías) vinculadas con la posibilidad de que una infección por SARS-CoV-2 se agrave, podrían hacerse análisis similares en poblaciones de otras partes del planeta. De este modo, los resultados podrían aprovecharse para mejorar los tratamientos que han surgido contra la enfermedad o, tras reconcocer posibles blancos que podrían ser explotados por cepas vigentes o futuras de SARS-CoV-2 y por ende podrían acrecentar la mortalidad del COVID-19, reforzar la vigilancia epidemiológica de este padecimiento (Rocha et al., 2025).  

<br>

## 4. Objetivo general

<!-- AYUDA: Expresen el resultado global mediante un verbo en infinitivo. Debe
ser alcanzable durante el semestre.
EJEMPLO: Desarrollar un flujo reproducible en Python para identificar y comparar
genes de resistencia en un conjunto de genomas de E. coli. -->

[Escriban aquí el objetivo general.]
Identificar si, entre los genomas de mexicanos que radican en EUA, está presente alguna de las variantes genéticas que se han reportado en relación con la susceptibilidad a desarrollar síntomas severos de COVID-19.

<br>

## 5. Preguntas de investigación

<!-- AYUDA: Formulen preguntas biológicas o computacionales que puedan
responderse con los datos y métodos disponibles. Indiquen qué evidencia sería
necesaria.
EJEMPLO: ¿Qué genes de resistencia aparecen en cada genoma? Evidencia: una tabla
de presencia y ausencia obtenida de las anotaciones. -->

### Pregunta 1

**Pregunta:** En los genomas de mexicanos que residen en Estados Unidos, ¿hay alguna variante genética patogénica o que incremente el riesgo de que surjan síntomas graves de COVID-19? En caso positivo, ¿en qué frecuencia está presente?

**Evidencia necesaria:** Genotipos presentes en las posiciones donde deberían ubicarse las variantes genéticas sobre cada cromosoma. A partir de estos datos, podrán tabularse y representarse las frecuencias de las variantes.

### Pregunta 2

**Pregunta:**  En los genomas anteriores, ¿existe alguna variante genética benigna, o candidata a serlo, respecto a la posibilidad de que un paciente que tenga COVID-19 muestre sintomatología severa? En caso positivo, ¿en qué frecuencia está presente?

**Evidencia necesaria:** Genotipos presentes en las posiciones donde deberían ubicarse las variantes genéticas sobre cada cromosoma. Luego, se tabularán y graficarán las frecuencias de las variantes.

<br>

## 6. Alcance y limitaciones

<!-- AYUDA: Delimiten organismos, muestras, datos, análisis y resultado esperado. Indiquen
qué no se abordará y las restricciones de tiempo, cómputo, acceso o calidad.
EJEMPLO: Se analizarán como máximo 20 genomas completos de RefSeq. No se
utilizarán datos clínicos ni se realizará validación experimental. -->

### Incluye

- Variantes genéticas (patogénicas, riesgosas, benéficas o candidatas a ser favorables) vinculadas con la susceptibilidad a exhibir síntomas graves de COVID-19. Esta información se tomará de ClinVar (NIH, s.f.), una exhaustiva base de datos clínica. 

- Genomas secuenciados de mexicanos que habitan en Estados Unidos. **Pendiente: Determinar con cuántos genomas se trabajará y en qué formato se descargarán (CRAM o FASTQ, así como las herramientas bioinformáticas para procesarlos).**

**Pendiente: Evaluar si, solo utilizando archivos CRAM o FASTQ, es viable trabajar con todos los tipos de variantes genéticas que impactan el desarrollo de sintomatología severa de COVID-19 (SNPs, deleciones, duplicaciones, inserciones y microsatélites).**

### No incluye

- Variantes genéticas que, según Clinvar, tienen una significancia incierta o que responden a medicamentos.

- Secuenciación de genomas a partir de muestras de pacientes.

- No se efectuarán validaciones experimentales.

### Limitaciones conocidas

- La población seleccionada (mexicanos que habitan en EUA), podría tener que reducirse a los residentes de Los Ángeles, California que cuentan con ancestría mexicana, puesto que esa es la comunidad de la cual se tienen datos fiables a gran escala (The International Genome Sample Resource, s.f.).

- La información sobre las variantes genéticas solo se obtendrá de ClinVar, que es una fuente actualizada con regularidad que detalla cuáles variaciones en el genoma están asociadas con alguna o múltiples enfermedades. Ello no implica que no existan otras bases de datos acerca de variantes genéticas de valor clínico. 


<br>

## 7. Propuesta de solución

<!-- AYUDA: Describan el producto o estrategia que podría resolver el problema.
Es una propuesta inicial y puede cambiar. Expliquen sus componentes, no sólo las
tecnologías.
EJEMPLO: Un programa modular recibirá identificadores, descargará archivos,
extraerá genes, almacenará resultados y generará visualizaciones. -->


**Esta es una propuesta, asumiendo que se trabajará con datos de archivos CRAM (lo cual parece agilizar la búsqueda de las variantes señaladas con anterioridad).**

Un programa modular recibirá un archivo sobre variantes genéticas, extraerá sus posiciones y el número del cromosoma al que pertenecen, revisará el genotipo que existe en el archivo CRAM y calculará las frecuencias de las variantes correspondientes. Estas últimas después podrán graficarse mediante Seaborn.

### 7.1 Resultado o producto esperado

<!-- AYUDA: Indiquen el entregable concreto: programa, paquete, flujo de análisis,
base de datos, visualizaciones u otro producto.
EJEMPLO: Repositorio ejecutable con scripts, datos de prueba, documentación,
tabla comparativa y figuras regenerables. -->

**Descripción tentativa***
Repositorio con scripts, datos de prueba, documentación y gráficas de las frecuencias de las variantes genéticas escogidas. 

## 8. Datos

### 8.1 Fuentes de datos

<!-- AYUDA: Incluyan institución, base de datos, URL, identificador, versión o
fecha de consulta y condiciones de uso. No todos los proyectos usarán NCBI.
EJEMPLO: NCBI RefSeq, GCF_000005845.2, consultado el dd/mm/aaaa. -->

| Fuente | Identificador o versión | URL | Fecha de consulta | Licencia o condiciones |
|:--|:--|:--|:--|:--|
| ClinVar | variant_summary.txt (no se indica su versión) | https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz | 22/08/2026 | N/A |
| IGSR | Data collections for Mexican Ancestry in Los Angeles, California. **Falta elegir el formato de los archivos y su versión.**  | https://www.internationalgenome.org/data-portal/population/MXL   | 28/08/26      | Debe citarse a IGSR si se usan los datos.  |

### 8.2 Características de los datos

<!-- AYUDA: Describan organismos, muestras, variables, formatos, versiones, tamaño y otros
atributos necesarios para interpretar los datos.
EJEMPLO: Archivos FASTA y GFF3 de 20 genomas completos de E. coli. -->


- Un documento de texto que contiene información sobre las variantes genéticas vinculadas con la susceptibilidad a presentar síntomas severos de COVID-19. Se descargó el 22/08/2026, pero no se especifica su versión.

- Archivos FASTA o CRAM de genomas de individuos que tienen ancestría mexicana y radican en Los Ángeles, California. **Aún falta determinar cuáles archivos se usarán.**


### 8.3 Organización de los datos

<!-- AYUDA: Muestren la estructura prevista. No suban datos sensibles, tokens,
contraseñas ni archivos grandes. Usen .gitignore y documenten cómo obtener lo
que no se guarde en Git.
EJEMPLO: data/raw conserva originales y data/processed los derivados. -->

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

### 8.4 Diccionario o formato de los datos

<!-- AYUDA: Describan campos o columnas relevantes. Incluyan fragmentos pequeños
cuando ayuden a comprender el formato, pero no archivos completos.
EJEMPLO: En GFF3, seqid identifica la secuencia; type indica gene, CDS, etc. -->

| Archivo o conjunto | Campo/columna | Tipo | Descripción | Valores o unidades |
|:--|:--|:--|:--|:--|
| variant_summary.txt.gz | AlleleID | Dato numérico | Identificador de cada variante genética | Entre 15041 y 4995437  |
| " " | Type | Dato categórico | Tipo de variante genética | Microsatellites, Deletion, Single Nucleotide Variant, ... |
| " " | ClinicalSignificance | Dato categórico | Relevancia clínica de la variante | Benign, Pathogenic, Likely risk allele, ... |
| " " | GenomeSymbol | Dato categórico | Nombre del gen asociado a la variante | STAT2, IRARK3, TLR7, MUC5B, HLA-G, IFNA10, ...|
| " " | PhenotypeList | Dato categórico | Enfermedades vinculadas a la variante | Susceptibility to severe COVID-19; Immunodeficiency 74, COVID-19-related, X-linked; ... |
| " " | Assembly | Dato numérico | Número de ensamble del genoma humano | NCBI36, GRCh38 o GRCh37 |
| " " | Chromosome | Dato alfanumérico | Número del cromosoma donde está la variante | Puede ser X, Y o un número entre 1 y 22 |
| " " | Start | Dato numérico | Posición donde empieza la variante | Pares de bases |
| " " | End | Dato numérico |  Posición donde termina la variante | Pares de bases |
| " " | ReferenceAlleleVCF | Cadena (str)  | Alelo habitual en la población | Combinación de 4 caractes ("A", "T", "G" y "C") |
| " " | AlternateAlleleVCF | Cadena (str) | Alelo anormal en la población | Combinación de 4 caractes ("A", "T", "G" y "C") |


**Falta precisar si se trabajará con archivos CRAM o FASTQ, así como los campos de cada tipo de documento.**

## 9. Metodología

<!-- AYUDA: Esta sección evolucionará. Primero describan el plan y después
actualícenla con lo que realmente ejecutaron, incluidos parámetros y decisiones. -->

### 9.1 Etapas del análisis o desarrollo

<!-- AYUDA: Describan la secuencia desde la obtención de datos hasta la validación
de resultados. Relacionen cada etapa con una pregunta u objetivo.
EJEMPLO: descarga, validación, transformación, análisis, visualización y pruebas. -->

1. [Etapa 1]
2. [Etapa 2]
3. [Etapa 3]


**Esbozo: Descarga de datos -> Validación de que estén completos -> Creación del archivo que solo contiene información sobre el COVID-19 -> Extracción de las posiciones de las variantes genéticas -> Búsqueda de esas variaciones entre los genotipos de los genomas mexicanos secuenciados -> Cálculo de las frecuencias de las variantes genéticas mencionadas -> Graficación de los resultados**

### 9.2 Herramientas y tecnologías

<!-- AYUDA: Registren lenguajes, bibliotecas y programas con sus versiones y
propósito. No incluyan credenciales.
EJEMPLO: Python 3.x; Biopython para leer formatos biológicos; Seaborn para
visualización. -->

| Herramienta | Versión | Propósito |
|:--|:--|:--|
| Processes (librería de Python) | 3.14.7 | Diseñar procesos para trabajar con herramientas de Unix diseñadas para manipular archivos CRAM o FASTQ |
| Seaborn (librería de Python) | 0.13.2 | Visualizar las frecuencias de las variantes genéticas en la población seleccionada |


**También se ocuparán herramientas de Bash para manipular archivos CRAM o FASTQ, pero aún es incierto cuál tipo de documentos se usarán.**

### 9.3 Estrategia de validación

<!-- AYUDA: Expliquen cómo comprobarán código y resultados: pruebas unitarias,
datos conocidos, comparación con otra herramienta o revisión manual.
EJEMPLO: Se compararán cinco anotaciones conocidas y se probarán entradas
válidas, identificadores inexistentes y archivos incompletos. -->

[Describan aquí la validación.]

**Pendiente. ¿Qué tipo de validaciones pueden hacerse?**

## 10. Plan de trabajo

#### *Esta sección solo muestra un esbozo. Tenemos dudas sobre las responsabilidades que deberíamos incluir aquí.*

### 10.1 Distribución de responsabilidades

<!-- AYUDA: Definan responsabilidades iniciales sin aislar a cada integrante.
Toda contribución importante debe ser revisada mediante Pull Request por otra
persona.
EJEMPLO: Ana desarrolla la descarga y revisa el módulo de visualización. -->

| Integrante | Responsabilidad principal | Responsabilidad de revisión |
|:--|:--|:--|
| Abril | Descarga de datos de ClinVar| Revisará, por checksum, que el archivo se haya descargado por completo |

**Aún falta distribuir responsabilidades, pero primero será imperativo determinar si se trabajará con archivos FASTQ o CRAM. En este momento, como se esbozó en el punto 7, parece que con el segundo tipo de archivos puede crearse un piepeline más eficiente.**

### 10.2 Riesgos y alternativas

<!-- AYUDA: Identifiquen situaciones que podrían impedir o retrasar el proyecto
y definan una alternativa.
EJEMPLO: Los datos requieren demasiado almacenamiento; alternativa: reducir el
número de genomas usando criterios documentados. -->

| Riesgo | Probabilidad | Impacto | Prevención o alternativa |
|:--|:--|:--|:--|
| [Riesgo] | Baja/Media/Alta | Bajo/Medio/Alto | [Acción] |
| [Riesgo] | Baja/Media/Alta | Bajo/Medio/Alto | [Acción] |

## 11. Resultados

<!-- AYUDA: Presenten resultados vinculados con preguntas y objetivos. Incluyan
tablas o figuras con títulos, leyendas y archivos de origen. Describan aquí lo
obtenido; interprétenlo en Discusión.
EJEMPLO: Tabla de presencia y ausencia generada por src/compare_genes.py.
PRIMERA SESIÓN: dejen esta sección como pendiente. -->

> Estado: pendiente. Se completará durante el desarrollo.



## 12. Discusión

<!-- AYUDA: Interpreten los resultados, expliquen si responden las preguntas,
compárenlos con los antecedentes y señalen limitaciones. No repitan únicamente
los valores.
EJEMPLO: La distribución observada sugiere..., aunque la interpretación está
limitada por la calidad de las anotaciones. -->

> Estado: pendiente. Se completará después de obtener resultados.

## 13. Conclusiones

<!-- AYUDA: Sinteticen qué se aprendió, qué preguntas se respondieron y si se
alcanzaron los objetivos. Incluyan aportes, limitaciones y trabajo futuro. No
introduzcan resultados nuevos.
EJEMPLO: El flujo permitió identificar..., pero será necesario incorporar... -->

> Estado: pendiente. Se completará al finalizar el proyecto.


## 14. Disponibilidad, licencia y citación

<!-- AYUDA: Indiquen dónde está el código, bajo qué licencia puede reutilizarse
y cómo citarlo. Relacionen esta sección con LICENSE, CITATION.cff, codemeta.json,
release final y, cuando corresponda, un DOI.
EJEMPLO: Código en GitHub bajo MIT; cita disponible en CITATION.cff. -->

**Código:** Almacenado en GitHub  
**Datos:** *Pendiente*  
**Licencia del código:** [MIT License](https://github.com/Mario-Samano/analisis_var_gene/blob/main/LICENSE)  
**Cómo citar:** *Pendiente*  
**Versión o release:** *Pendiente* 

## 15. Referencias

<!-- AYUDA: Registren publicaciones, datos, software y documentos consultados en
un formato uniforme. Incluyan DOI, URL o identificadores persistentes. Toda cita
del texto debe aparecer aquí.
EJEMPLO: Blattner, F. R. et al. (1997). The complete genome sequence of
Escherichia coli K-12. Science, 277(5331), 1453–1462.
https://doi.org/10.1126/science.277.5331.1453 -->


1. Chakraborty, C., Bhattacharya, M., Chatterjee, S., Lee, S.S., Bhattacharya, P., Ohimain, E.I., Wen, Z. Das, A., Rai, A., Abdelhameed, A.S., Agoramoorthy, G., Zayed, H., Byrareddy, S.N. (2025). Comprehensive global-scale evaluation of the COVID-19 pandemic associated with 234 countries, territories, and sub-national locations during 2020–2024. *Folia Microbiologica*. https://doi.org/10.1007/s12223-025-01299-9

2. Cross, G. (2026, 11 de marzo). *6 years since COVID-19 pandemic began. What happened March 11, 2020* [sic]. USA Today. https://www.usatoday.com/story/news/nation/2026/03/11/covid-19-pandemic-march-11-2020/89082810007/

3. Fabrizio, C., Termine, A., Caputo, V., Megalizzi, D., Calvino, G., Trastulli, G., Ingrascì, A., Ferrante, S., Peconi, C., Rossini, A., Salvia, A., Caltagirone, C., Strafella, C., Giardina, E., & Cascella, R. (2022). Analysis of Genetic Variants Associated with COVID-19 Outcome Highlights Different Distributions among Populations. *Journal of personalized medicine, 12* (11), 1851. https://doi.org/10.3390/jpm12111851

4. Giné-Garriga, R., Delepiere, A., Ward, R., Alvarez-Sala, J., Alvarez-Murrillo, I., Mariezcurrena, V., Göransson Sandberg, H., Saikia, P., Avello, P., Thakar, K., Ibrahim, E., Nuvellon, A., El Hattab, O., Hutton, G., Jimenez, A. (2021). COVID-19 water, sanitation, and hygiene response: Review of measures and initiatives adopted by governments, regulators, utilities, and other stakeholders in 84 countries. *Science of 4. the Total Environment, 795* (15), 148789. https://doi.org/10.1016/j.scitotenv.2021.148789

5. Gong, Z., Song, T., Hu, M. Che, Q., Guo, J., Zhang, H., Li, H., Wang, Y., Liu, B., Shi, N. (2024). Ntural and socio-environmental factors in the transmission of COVID-19: a comprehensive analysis of epidemiology and mechanisms. *BMC Public Health, 24,* 2196. https://doi.org/10.1186/s12889-024-19749-3

6. Montero R,I., Dionicio, C.L., Noris, G., Piña-Pozas, M., Santana, C., Gómez, R. (2025) Genetic variants in TMPRSS2 influence SARS-CoV-2 infection susceptibility within Mexican Mestizos. *Frontiers in Genetics, 16*, 1558189. https://doi.org/10.3389/fgene.2025.1558189

7. National Institutes of Health (s.f.). Index of /pub/clinvar/tab_delimited. ClinVar. Consultado el 22 de agosto del 2026. https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz

8. Riley, A.R., Chen, Y.H., Matthay, E.C., Glymour, M.M., Torres, J.M., Fernandez, A., Bibbins-Domingo, K. (2021). Excess mortality among Latino people in California during the COVID-19 pandemic. *SSM - Population Health, 15*, 100860. https://doi.org/10.1016/j.ssmph.2021.100860

9. Rocha G.D., Oliveira, P.R.S., de Oliveira Sá, M.V.B., de Lima Campos, T., Galdino Galisa, S.L., Silva, A.S., Moura, P., de São Pedro, R.B., Tavares, N.M., Boaventura, V.S., Nunes, S., Bonyek-Silva, I., Caldas, J.R., Roma, E.H., Almeida, J.R., Silva, A.A., Baccin, T., de Castro, A.C., Vallinoto, A.C.R, da Silva, R., Dos Santos, E.J.M., Garcia, C.C., Slhessarenko, R.D., da Costa Armstrong, A., do Carmo, R.F., Vasconcelos, L.R.S. Rare genetic variants and severe COVID-19 in previously healthy admixed Latin American adults. *Scientific Reports, 15* (1), 23074. https://doi.org/10.1038/s41598-025-08416-1 

10. Secolin, R., de Araujo, T.K., Gonsales, M.C., Rocha, C.S.,Naslavsky, M., Marco, L., Bicalho, M.A.C., Vazquez, V.L., Zatz, M., Silva, W.A., Lopes-Cendes, I. (2021). Genetic variability in COVID-19-related genes in the Brazilian population. *Human Genome Variation, 8*, (15). https://doi.org/10.1038/s41439-021-00146-w

11. Shikov A.E., Barbitoff, Y.A., Glotov, A,S., Danilova, M.M., Tonyan, Z.N., Nasykhova, Y.A., Mikhailova, A.A., Bespalova, O.N., Kalinin, R.S., Mirzorustamova, A.M., Kogan, I.Y., Baranov, V.S., Chernov, A.N., Pavlovich, D.M., Azarenko, S.V., Fedyakov. M.A., Tsay, V.V., Eismont, Y.A., Romanova, O.V., Hobotnikov, D.N., Vologzhanin, D.A., Mosenko, S.V., Ponomareva, T.A., Talts, Y.A., Anisenkova, A.U., Lisovets, D.G., Sarana, A.M., Urazov, S.P., Scherbak, S.G., Glotov, O.S. (2020) Analysis of the Spectrum of ACE2 Variation Suggests a Possible Influence of Rare and Common Variants on Susceptibility to COVID-19 and Severity of Outcome. *Frontiers in Genetics, 11* (28), 551220. https://doi.org/10.3389/fgene.2020.551220

12. The International Genome Sample Resource (s.f.). *Population: Mexican Ancestry in Los Angeles, California.* IGSR: The International Genome Sample Resource. Consultado el 28 de agosto del 2026. https://www.internationalgenome.org/data-portal/population/MXL



---

<!-- ORIENTACIÓN PARA LAS DOS PRIMERAS SESIONES:
Completen Información general, Resumen provisional, secciones 1 a 7, fuentes de
datos preliminares y plan de trabajo. Metodología, Resultados, Discusión,
Conclusiones Y Disponibilidad evolucionarán durante el
semestre. Sustituyan las indicaciones entre corchetes por contenido del equipo. -->
