# comparative-genomics

RASTtk ANNOTATION
rast_tk.py

Se corre en el directorio donde se encuentran, en formato fasta, los genomas que se quieren anotar (cepas/). El programa toma como input todos los genomas del directorio que terminen en “.fasta” y devuelve como output los archivos de anotación correspondientes en formato genbank_merged (“.gbk”). 
Este formato es requerido por eCAMBer, permite tener las anotaciones en posiciones genómicas sucesivas y no en start y ends partidos por cada contig. El nombre del archivo gbk que se genera se corresponderá al del fasta de inicio.



eCAMBer comparative analysis of multiple bacterial strains within the same species
gbk_2_ecamber.py, run_ecamber.py

Para preparar el dataset que será input del análisis con eCAMBer se deberá correr gbk_2_ecamber.py primero.
Se debe crear un directorio nuevo dentro de la carpeta “datasets/” del directorio “ecamber/”, que es donde se encuentra el programa ecamber.py

En el directorio creado (ecamber/dataset/ejemplo/) deben estar los genomas en formato gbk_merged anotados con RASTtk. El programa toma como input los gbk y devuelve como output: un directorio conteniendo los archivos de anotación en formato texto (ecamber/datasets/ejemplo/anss_parsed/), otro directorio que contiene los genomas en formato fasta (ecamber/datasets/ejemplo/genomes/) y un archivo de texto que contiene los nombres de los genomas a ser analizados (strains.txt).

Una vez preparado el dataset se corre run_ecamber.py que ejecuta en línea de comando los argumentos del programa eCAMBer que toman como input el dataset generado y devuelven como output diversos directorios, en particular output es con que seguiremos trabajando. Para esto debemos modificar el nombre del [directorio] en el script.

