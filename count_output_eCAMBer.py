#!/usr/bin/env python

import sys
import os
import fileinput

file = sys.argv[1]	#cluster_table.txt

core_genome = 0
cluster_unicos = 0
pangenoma = 0

for line in fileinput.input(file):
  campo = line.strip().split('\t')
  if line.startswith("cluster_id"):
    total_genomes = len(campo[7:int(len(campo))])
  else:
    pangenoma += 1
  
  cluster_id = campo[0]
  cluster_strain_count = campo[5]
  cluster_strain_ann = campo[6]

  if cluster_strain_count == str(total_genomes):
    core_genome += 1	  
  if cluster_strain_count == '1':
    cluster_unicos += 1

print 'Core-genoma: ', core_genome			#The core-genome contains gene families shared by all the organisms
print 'Pangenome: ', pangenoma				#Full complement of genes in a list of organisms
print 'Genome specific genes: ', cluster_unicos		#Strain specific genes 

