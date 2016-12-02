import numpy as np
import re

nodefile = open('example.node','rw').readlines()
elefile = open('example.ele','rw').readlines()

# Declares arrays for nodes and triangles.
tripts = np.empty([1,3]) # x coord, y coord, boundary?
tridefs = np.empty([1,3]) # point 1, point 2, point 3

# Parses the output files.
del nodefile[0]
for linea in nodefile:
    linea = re.split(' +',linea)
    for i in range(1,4):
        print linea[i]
    del linea[0]
    tripts = np.append(tripts,[[float(linea[1]),float(linea[2]),float(linea[4])]],0)
tripts = np.delete(tripts, 0, 0)

del elefile[0]
for linea in elefile:
    linea = re.split(' +',linea)
    for i in range(1,4):
        print linea[i]
    del linea[0]
    tridefs = np.append(tridefs,[[float(linea[1]),float(linea[2]),float(linea[3])]],0)
tridefs = np.delete(tridefs, 0, 0)

print("\n\n\n")

print tripts
print tridefs