#!/usr/bin/env python

#creo directorios
#genero archivos de anotacion y los multifastas a partir de gbks
#genero el archivo de cepas strains.txt
#muevo los archivos de anotacion a la carpeta de anotaciones y los archivos multifasta a la carpeta de genomas

import sys
import os
import fileinput
import pprint

from Bio import SeqIO
from Bio import Seq

# PARA ARCHIVOS GBK exportados con el rasttk genero los archivos de anotacion 
filename = os.listdir(".")
for file in filename:
  if file.endswith('.gbk'):
    name = file.split('.')[0]
    for record in SeqIO.parse(file, "genbank"):
      record.id = name
      SeqIO.write(record, name + '.fasta', "fasta")
      CDS = [ f for f in record.features if f.type=="CDS"]
      for item in CDS:
        gene_id = item.qualifiers.get("db_xref")[0].replace("RAST2:","")
        hebra = str(item.strand).replace("-1","-").replace("1","+")
        start = (item.location).nofuzzy_start + 1
        end = (item.location).nofuzzy_end
        gene_name = item.qualifiers.get("product")[0].replace(" ","_")
        f = open(name + '.txt', "a")
        f.write(gene_id +'\t'+ str(start) +'\t'+ str(end) +'\t'+ hebra +'\t'+ gene_name + '\n')
        f.close()

#creo la lista de strains en formato txt
filename = os.listdir(".")
f = open('strains.txt', "a")  
for file in filename:
  if file.endswith('.fasta'):
    f.write(file.split('.')[0] + '\n')
f.close()
      
#crea, si no existen, los directorios anns_parsed y genomes 
if not os.path.exists('anns_parsed/patric/'):
  os.makedirs('anns_parsed/patric/')
if not os.path.exists('genomes/'):
  os.makedirs('genomes/')

#muevo los archivos txt generados para cada anotacion a la carpeta creada
filename = os.listdir(".")
for file in filename:
  if file.endswith('.txt'):
    if file != 'strains.txt':
      os.system('mv ' + file + ' anns_parsed/patric/')
  if file.endswith('.fasta'):
    os.system('mv ' + file + ' genomes/')
