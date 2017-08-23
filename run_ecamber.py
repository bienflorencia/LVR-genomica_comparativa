#!/usr/bin/env python

import sys
import os

#comandos para correr ecamber.py a partir del [directorio] de genomas 
os.system('python ecamber.py -a f -d [directorio] -w 4')
os.system('python ecamber.py -a ph1 -d [directorio] -w 4 -as patric')
os.system('python ecamber.py -a ph2 -w 4 -d [directorio] -as patric')
os.system('python ecamber.py -a out -d [directorio] -w 4 -as patric -step 3')
