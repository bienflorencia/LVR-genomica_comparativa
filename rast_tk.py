#!/usr/bin/env python

import sys
import os

filename = os.listdir(".")

for archivos in filename:
    if archivos.endswith(".fasta"):
      name = archivos.split('.')
      os.system("rast-create-genome --scientific-name "'Salmonella enterica subsp. enterica serovar Typhimurium'" --domain Bacteria --genetic-code 11 --ncbi-taxonomy-id 90371 --contigs " + archivos + " | rast-process-genome > " + name[0] + ".gto")

filename = os.listdir(".")

for archivos in filename:
  if archivos.endswith(".gto"):
    name = archivos.split('.')
    os.system("rast-export-genome genbank_merged < " + archivos + " > " + name[0] + ".gbk")

