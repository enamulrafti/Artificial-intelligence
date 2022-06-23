from google.colab import drive
drive.mount('/content/gdrive')
from numpy import genfromtxt


data_path='/content/gdrive/MyDrive/AI/iris.csv'
my_data=genfromtxt(data_path,delimiter=',')

data=my_data.tolist()

train_set=[]
val_set=[]
test_set=[]

import random
random.shuffle(data)

for x in data:
  R=random.uniform(0, 1)
  if R>=0 and R<=0.7:
    train_set.append(x)
  elif R>0.7 and R<=0.85:
    val_set.append(x)
  else:
    test_set.append(x)

import numpy


aa=numpy.array(train_set)
ab=numpy.array(val_set)

j=0
k=15
correct=0

for V in val_set:
  i=0
  L=[]
  for T in train_set:
    a2=numpy.array(aa[i,:-1])
    a3=numpy.array(ab[j,:-1])
    dist = numpy.linalg.norm(a3-a2)
    L.append((T,dist))
    i=i+1
  L.sort(key = lambda x: x[1])
  L2=[]
  for xx in range(k):
     k2=L[xx][0]
     L2.append(k2)
  arr = numpy.array(L2)
  y=arr[:,-1]
  newarr = y.astype(int)
  m=numpy.bincount(newarr).argmax()
  arr4 = numpy.array(V)
  arr5=arr4.tolist()
  b=arr5[-1]
  if b==m:
    correct=correct+1
  j=j+1

val_acc=(correct/len(val_set))*100
print(val_acc)




