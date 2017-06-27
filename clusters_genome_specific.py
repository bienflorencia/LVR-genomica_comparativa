#!/usr/bin/env python

#Este script tienen como argumentos la lista de archivos txt de cada cluster y el archivo de genomas especificos que quiero evaluar (./clusters_genome_specific.py "output/clusters/*")
#A partir de esa lista de genomas busca entre los clusters y me devuelve en un archivo de texto (clusters_genome_specific.txt) aquellos en los que solo se encuentran los genomas listados en group.txt

import sys
import os
import fileinput
import glob

sys.stdout=open("clusters_genome_specific.txt","w")

file1 = sys.argv[1]
lista_genomas = []
dic_genomes = {}

f = open("group.txt", "r")
for line in f:
  genoma = line.strip('\n')
  lista_genomas.append(genoma)

for file in glob.glob(file1):
  filename = fileinput.input(file)
  for line in filename:
    if line.startswith('>'):
      cluster = line.split('|')[-6]
      genome = line.strip('\n').split('|')[-1]
      if cluster in dic_genomes:
        lista = dic_genomes[cluster]
        if genome not in lista:
          lista.append(genome)
          dic_genomes[cluster] = lista
      else:
          dic_genomes[cluster] = [genome]

for k, v in dic_genomes.iteritems():
  if sorted(v) == sorted(lista_genomas):
    print k

