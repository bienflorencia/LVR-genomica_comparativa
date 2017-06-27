#!/usr/bin/env python

import sys
import os
import fileinput

##Este script se corre solo y con la tabla de clusters como segundo argumento

#archivo cluster_table.txt
file = sys.argv[1]

sys.stdout=open("clusters_matrix.txt","w")

dicCluster = {}
for line in fileinput.input(file):
  campo = line.strip('\n').split('\t')
  genomes = campo[7:int(len(campo)-1)] 
  if line.startswith('cluster'):
    header = '\t'.join(map(str,genomes))
    print 'cluster\t'+header 
  else:
    cluster_id = int(campo[0]) 
    dicCluster[cluster_id] = genomes

#matriz de presencia ausencia
dicGenomes = {}
for k, v in dicCluster.iteritems():
  a = []
  if k != 0:
    for gene in v:
      if gene == '':
	a.append(0)
      else:
	a.append(1)
    dicGenomes[k] = a

#imprime la tabla con cluster, genomas y 1-0
for k, v in sorted(dicGenomes.items()):
  valores = '\t'.join(map(str,v))
  print str(k)+'\t'+str(valores)
		
sys.stdout.close()


