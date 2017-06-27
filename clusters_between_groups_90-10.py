#!/usr/bin/env python

import sys
import os
import fileinput
import glob

#sys.stdout=open("clusters_group_specific.txt","w")

file1 = sys.argv[1]
lista1_genomas = []
lista2_genomas = []
dic_clusters = {}

porcentaje_si = 0.90
porcentaje_no = 0.10

f = fileinput.input("group1.txt")
for line in f:
  genoma = line.strip('\n')
  lista1_genomas.append(genoma)
total_lista1 = len(lista1_genomas)

g = fileinput.input("group2.txt")
for line in g:
  genoma = line.strip('\n')
  lista2_genomas.append(genoma)
total_lista2 = len(lista2_genomas)

for file in glob.glob(file1):
  filename = fileinput.input(file)
  for line in filename:
    if line.startswith('>'):
      cluster = line.split('|')[-6]
      genome = line.strip('\n').split('|')[-1]
      if genome in dic_clusters:
	lista = dic_clusters[genome]
	if cluster not in lista:
	  lista.append(cluster)
	  dic_clusters[genome] = lista
      else:
	  dic_clusters[genome] = [cluster]


lista_g1 = []
lista_g2 = []

# ESTO OTRO SERIA PARA CLUSTERS DEL COREGENOMA

coregenome = {}
lista2 = {}


for k, v in dic_clusters.iteritems():
  if k in lista1_genomas:
    for value in v:
      if value in coregenome:	
	coregenome[value] += 1
      else:
	coregenome[value] = 1
  if k in lista2_genomas:
    for value in v:
      if value in lista2:	
	lista2[value] += 1
      else:
	lista2[value] = 1
	
dic_gene_names = {}
h = fileinput.input("cluster_gene_names.txt")
for line in h:
  genoma = line.strip('\n').split('\t')
  dic_gene_names[genoma[0]] = genoma[1]

for item, val in coregenome.iteritems():
  if item in coregenome.keys() and (val >= (total_lista1*porcentaje_si)):
    for items, vals in lista2.iteritems():
      if item == items and (vals <= (total_lista2*porcentaje_no)):
	if item in dic_gene_names.keys():
	  print item, dic_gene_names[item], val, vals

    

