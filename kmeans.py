import pandas as pd
import math as mt
import matplotlib.pyplot as plt
c=[]
point=[]
clstr_point=[]
c_fin=[]
data=pd.read_csv("data.csv") 
i=0
X=[]
Y=[]

while i<len(data.X):
    X.append(data.X[i])
    Y.append(data.Y[i])
    clstr_point.append([])
    clstr_point[i].append(data.X[i])
    clstr_point[i].append(data.Y[i])
    clstr_point[i].append(0)
    i=i+1;
i=0
n=int(input("No of centroids"))
cord_sc_x=[]
cord_sc_y=[]
while i<n:
    a=input("X-cord of"+str(i+1)+"th centroid")
    b=input("Y-cord of"+str(i+1)+"th centroid")
    c_fin.append([])
    c_fin[i].append(a)
    c_fin[i].append(b)
    c.append([])
    c[i].append(a)
    c[i].append(b)
    point.append(1)
    cord_sc_x.append([])
    cord_sc_y.append([])
    i=i+1

i=0

while i<len(data.X):
    j=0
    pos=0
    minn=9999.01
    while j<len(c):   
        length=mt.sqrt(mt.pow(X[i]-float(c_fin[j][0]),2)+mt.pow(Y[i]-float(c_fin[j][1]),2))
        if length<minn:
            minn=length
            pos=j
        j=j+1
    
    point[pos]=point[pos]+1
    c[pos][0]=(float(c[pos][0])+X[i])
    c_x=float(c[pos][0])/(point[pos])
    c[pos][1]=(float(c[pos][1])+Y[i])
    c_y=float(c[pos][1])/(point[pos])
    c_fin[pos][0]=c_x
    c_fin[pos][1]=c_y
    i=i+1;

    

i=0

while i<len(data.X):
    j=0
    pos=0
    minn=9999
    while j<len(c):   
        length=mt.sqrt(mt.pow(X[i]-c_fin[j][0],2)+mt.pow(Y[i]-c_fin[j][1],2))
        if length<minn:
            minn=length
            pos=j
        j=j+1   
    clstr_point[i][2]=pos
    i=i+1;



i=0
print("X         Y        C")
while i<len(X):
    print(str(clstr_point[i][0])+"\t"+str(clstr_point[i][1])+"\t"+str(clstr_point[i][2]+1))
    cord_sc_x[clstr_point[i][2]].append(clstr_point[i][0])
    cord_sc_y[clstr_point[i][2]].append(clstr_point[i][1])
    i=i+1
    

i=0
while i<n:
    plt.scatter(cord_sc_x[i],cord_sc_y[i])
    i=i+1
plt.show()