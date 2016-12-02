import numpy as np
import io
import os
import re

os.system('touch example.poly')
fila = open('example.poly','w')
tripts = np.empty([1,4])
edgedef = np.empty([1,3])
holedef = np.empty([1,3])

i = 0
l = 0
data = "0"
while(data != ""):
    data = raw_input("X? Y? Height? Width?\n")
    if(data == ""):
        continue
    data = re.split(" +", data)
    tripts = np.append(tripts,[[4*i+1,float(data[0]),float(data[1]),0]],0)
    tripts = np.append(tripts,[[4*i+2,float(data[0]),float(data[1])+float(data[2]),0]],0)
    tripts = np.append(tripts,[[4*i+3,float(data[0])+float(data[2]),float(data[1]),0]],0)
    tripts = np.append(tripts,[[4*i+4,float(data[0])+float(data[2]),float(data[1])+float(data[2]),0]],0)
    edgedef = np.append(edgedef,[[4*l+1,i,i+1]],0)
    edgedef = np.append(edgedef,[[4*l+2,i,i+2]],0)
    edgedef = np.append(edgedef,[[4*l+3,i+1,i+3]],0)
    edgedef = np.append(edgedef,[[4*l+4,i+2,i+3]],0)
    holedef = np.append(holedef,[[i,float(data[0])+0.5*float(data[3]),float(data[1])+0.5*float(data[2])]],0)
    i += 1
    l += 1

tripts = np.delete(tripts,0,0)
edgedef = np.delete(edgedef,0,0)
holedef = np.delete(holedef,0,0)
print(len(tripts))
print(len(edgedef))
print(len(holedef))
print(tripts)

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

#for i in range(0,len(tripts)):
#    print(tripts[i],"")
#print("\n\n")
#for i in range(0,len(edgedef)):
#    print(edgedef[i],"")
#print("\n\n")
#for i in range(0,len(holedef)):
#    print(holedef[i],"")