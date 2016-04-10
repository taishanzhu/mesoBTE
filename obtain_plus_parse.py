import numpy as np
from math import pi
from math import sin
from math import cos
import io
import os
import re

# Sets up the file and the arrays.
os.system('touch example.poly')
fila = open('example.poly','w')
tripts = [[0,0,0,0]]
edgedef = [[0,0,0]]
holedef = [[0,0,0]]

# Begins taking input about polygons.
i = 1
l = 0
data = "0"
while(data != ""):
    data = raw_input("X? Y? Num? Rad?\n")
    if(data == ""):
        continue
    data = re.split(" +", data)
    equis = float(data[0])
    igriega = float(data[1])
    num = int(data[2])
    rad = float(data[3])
    for ang in range(0,num):
        tripts.append([l+ang+1,equis+cos(2*pi*ang/num),igriega+sin(2*pi*ang/num),0])
    for ang in range(0,num):
        edgedef.append([l+ang+1,l+ang+1,l+((ang+2) if (ang!=num-1) else 1)])
    holedef.append([i,float(data[0]),float(data[1])])
    i += 1
    l += num
tripts.append([l+1,tripts[np.argmin(tripts,axis=0)[1]][1]-1,tripts[np.argmin(tripts,axis=0)[2]][2]-1,1])
tripts.append([l+2,tripts[np.argmin(tripts,axis=0)[1]][1]-1,tripts[np.argmax(tripts,axis=0)[2]][2]+1,1])
tripts.append([l+3,tripts[np.argmax(tripts,axis=0)[1]][1]+1,tripts[np.argmax(tripts,axis=0)[2]][2]+1,1])
tripts.append([l+4,tripts[np.argmax(tripts,axis=0)[1]][1]+1,tripts[np.argmin(tripts,axis=0)[2]][2]-1,1])
edgedef.append([l+1,l+1,l+2,1])
edgedef.append([l+2,l+2,l+3,1])
edgedef.append([l+3,l+3,l+4,1])
edgedef.append([l+4,l+4,l+1,1])

# Excises nonsense and writes file in appropriate format.
tripts.pop(0)
edgedef.pop(0)
holedef.pop(0)
file = [str(int(len(tripts)))+' 2 0 1\n']
for k in range(0,len(tripts)):
    file.append(str(int(tripts[k][0]))+" "+str(tripts[k][1])+" "+str(tripts[k][2])+" "+str(int(tripts[k][3]))+'\n')
file.append(str(len(edgedef))+" 1\n")
for k in range(0,len(edgedef)):
    file.append(str(int(edgedef[k][0]))+" "+str(int(edgedef[k][1]))+" "+str(int(edgedef[k][2]))+'\n')
file.append(str(len(holedef)-1)+"\n")
for k in range(0,len(holedef)):
    file.append(str(int(holedef[k][0]))+" "+str(holedef[k][1])+" "+str(holedef[k][2])+'\n')
fila.writelines(file)

# Outsources computation to 'triangle'.
os.system('triangle -p -q -n -e example.poly')
nodefile = open('example.node','rw').readlines()
elefile = open('example.ele','rw').readlines()
neighfile = open('example.neigh','rw').readlines()
edgefile = open('example.edge','rw').readlines()

# Declares arrays for nodes and triangle definitions.
tripts = [[0,0,0]] # x coord, y coord, boundary?
tridefs = [[0,0,0]] # point 1, point 2, point 3
neighdefs = [[0,0,0]] # neighbor 1, neighbor 2, neighbor 3
edgepts = [[0,0,0]] # endpt 1, endpt 2, boundary?

# Parses the output files.
del nodefile[0]
for linea in nodefile:
    linea = re.split(' +',linea)
    del linea[0]
    tripts.append([float(linea[1]),float(linea[2]),float(linea[4])])

del elefile[0]
for linea in elefile:
    linea = re.split(' +',linea)
    del linea[0]
    tridefs.append([float(linea[1]),float(linea[2]),float(linea[3])])

del neighfile[0]
for linea in neighfile:
    linea = re.split(' +',linea)
    del neighfile[0]
    tridefs.append([int(linea[1]),int(linea[2]),int(linea[3])])
    
del edgefile[0]
for linea in edgefile:
    linea = re.split(' +',linea)
    del linea[0]
    tridefs.append([float(linea[1]),float(linea[2]),int(linea[3])])
