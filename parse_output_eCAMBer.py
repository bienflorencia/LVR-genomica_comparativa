#!/usr/bin/env python
#Esta es la revision que hizo BD pero da el mismo resultado.
import sys
import os
import fileinput

##Este script se corre solo y con la tabla de clusters como segundo argumento

#archivo cluster_table.txt
file = sys.argv[1]

#depende de la cantidad de genomas analizados se puede elegir la opcion que pregunta cuantos genomas (rawinput)

#fin = 7 + int(raw_input('Total de genomas considerados en el analisis: '))

sys.stdout=open("clusters_matrix.txt","w")

#dicCluster = {}
#for line in fileinput.input(file):
#  campo = line.strip('\n').split('\t')
#  cluster_id = campo[0] 
#  genomes = campo[7:fin]
#  if line.startswith('cluster'):
#    header = str(genomes).replace("[","").replace("]","").replace("'","").replace(",","\t")
#    print '\t', header
#  else:
#    dicCluster[cluster_id] = []
#    lista = genomes
#    for k in dicCluster.keys():
#      dicCluster[cluster_id] = lista
dicCluster = {}
for line in fileinput.input(file):
  campo = line.strip('\n').split('\t')
  #cluster_id = int(campo[0])  #lo pongo mas abajo
  genomes = campo[7:int(len(campo)-1)] #esto elimina la necesidad de ingresar el numero de genomas.
  if line.startswith('cluster'):
    header = '\t'.join(map(str,genomes))
    print 'cluster\t'+header #OJO: cuando pones "," en el print, lo que hace es separar con un espacio
  else:
    cluster_id = int(campo[0])  #si los cluster_id van a ser numericos, conviene que sean codificados como numero para el sort final
    #las lineas comentadas de abajo no son necesarias:
    #dicCluster[cluster_id] = []
    #lista = genomes
    #for k in dicCluster.keys():
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
  print str(k)+'\t'+str(valores) #aca todos los valores van como string para que funcione el "+", de otra forma python intenta sumar los enteros y da error.
                                 #De hecho, se podria imprimir la suma de genomas que tiene cada cluster, haciendo sum(valores), en una columna extra.
sys.stdout.close()


