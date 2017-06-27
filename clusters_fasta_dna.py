#!/usr/bin/env python

#Se corre './clusters_fasta_dna.py output/cluster_gene_names.txt "genes_dna/*.fasta"'

#Este script me devuelve una lista de genes, con sus secuencias fasta, anotados por cada genoma
#Es decir por cada cluster genera un archivo (ej:cluster_1.txt) que contiene la secuencia fasta del gen A del genoma 1, gen B del genoma 2, gen C del genoma 3, etc.

import sys
import os
import fileinput
import glob

from Bio import SeqIO
from Bio import Seq

file1 = sys.argv[1]		#archivo "output/cluster_gene_names.txt"
file2 = sys.argv[2]		#archivos "genes_dna/*.fasta"

#crea, si no existe, el directorio clusters

if not os.path.exists('clusters/'):
  os.makedirs('clusters/')

lista_clusters = []
for line in open(file1).readlines():
	campo = line.split('\t')
	lista_clusters.append(campo[0])

for file in glob.glob(file2):
	filename = fileinput.input(file)
	for record in SeqIO.parse(filename, 'fasta'):
   		cluster = record.name.split('|')[-6]
		f = open('clusters/'+ cluster +'.fasta', 'a')		#crear el directorio "output/clusters/" dentro del output
  		if cluster in lista_clusters:
			f.write(str('>' + record.name +'\n'+ record.seq +'\n\n'))
		f.close()


