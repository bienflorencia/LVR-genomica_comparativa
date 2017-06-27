# comparative-genomics

##RASTtk anotación de genomas
rast_tk.py

Se corre en el directorio donde se encuentran, en formato fasta, los genomas que se quieren anotar (cepas/). El programa toma como input todos los genomas del directorio que terminen en “.fasta” y devuelve como output los archivos de anotación correspondientes en formato genbank_merged (“.gbk”). 
Este formato es requerido por eCAMBer, permite tener las anotaciones en posiciones genómicas sucesivas y no en start y ends partidos por cada contig. El nombre del archivo gbk que se genera se corresponderá al del fasta de inicio.


##eCAMBer comparative analysis of multiple bacterial strains within the same species
gbk_2_ecamber.py, run_ecamber.py

Para preparar el dataset que será input del análisis con eCAMBer se deberá correr gbk_2_ecamber.py primero.
Se debe crear un directorio nuevo dentro de la carpeta “datasets/” del directorio “ecamber/”, que es donde se encuentra el programa ecamber.py

En el directorio creado (ecamber/dataset/ejemplo/) deben estar los genomas en formato gbk_merged anotados con RASTtk. El programa toma como input los gbk y devuelve como output: un directorio conteniendo los archivos de anotación en formato texto (ecamber/datasets/ejemplo/anss_parsed/), otro directorio que contiene los genomas en formato fasta (ecamber/datasets/ejemplo/genomes/) y un archivo de texto que contiene los nombres de los genomas a ser analizados (strains.txt).

Una vez preparado el dataset se corre run_ecamber.py que ejecuta en línea de comando los argumentos del programa eCAMBer que toman como input el dataset generado y devuelven como output diversos directorios, en particular output es con que seguiremos trabajando. Para esto debemos modificar el nombre del [directorio] en el script.


Generación de matriz de clusters de ortólogos
parse_output_eCAMBer.py 

A partir de la tabla de clusters como input ("clusters_table.txt") se obtiene como output la matriz de presencia (1) y ausencia (0) de los ortólogos por cada genoma. La tabla de clusters se encuentra dentro de la carpeta output.


Descripción de los grupos de ortólogos 
count_output_eCAMBer.py

Este script nos permite conocer el coregenoma, pangenoma y los genes de genomas específicos. El coregenoma representa aquellos genes que están presentes en todos los genomas, el pangenoma es el conjunto de genes anotados del total de genomas analizados, y los genes específicos son aquellos que se encuentran únicamente para uno de los genomas.


Generación de clusters de ortólogos 
clusters_fasta_dna.py

A partir de los archivos fasta para cada genoma se obtienen los archivos fasta para cada cluster. Precisa como input la tabla de clusters y los archivos fasta para cada genoma que se encuentran en el directorio de output (genes_dna/), y devuelve como output un directorio conteniendo un archivo txt para cada cluster. Se corre ./clusters_fasta_dna.py clusters_table.txt “output/genes_dna/*.fasta”

Es decir, por cada cluster genera un archivo (ej: cluster_1.fasta) que contiene la secuencia fasta del gen 1 del genoma A, gen 1 del genoma B, gen 1 del genoma C, etc.


Análisis de genes específicos de un grupo de genomas
1- Estricto clusters_genome_specific.py
2- Entre grupos clusters_between_groups_90-10.py


clusters_genome_specific.py

A partir de los archivos de las secuencias fasta para cada cluster podemos analizar cuáles son los clusters que contienen copias únicamente de un grupo de genomas específico. Para esto precisamos como inputs la lista de archivos fasta de cada cluster ("output/clusters/*") y el archivo de genomas específicos que quiero evaluar (group.txt). A partir de esa lista de genomas busca entre los clusters y me devuelve en un archivo de texto (clusters_genome_specific.txt) aquellos en los que solo se encuentran los genomas listados en group.txt.
Se corre como ./clusters_genome_specific.py "clusters/*" group.txt


clusters_between_groups_90-10.py






