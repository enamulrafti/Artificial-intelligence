from google.colab import drive
drive.mount('/content/gdrive')
from numpy import genfromtxt

data_path='/content/gdrive/MyDrive/AI/diabetes.csv'
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
error=0


for V in val_set:
  i=0
  L=[]
  for T in train_set:
    a2=numpy.array(aa[i,:-1])
    a3=numpy.array(ab[j,:-1])
    dist = numpy.linalg.norm(a3-a2)
    L.append((T,dist))
    L.sort(key = lambda x: x[1])
    i=i+1
  L2=[]
  for xx in range(k):
     k2=L[xx][0]
     L2.append(k2)
  arr = numpy.array(L2)
  y=arr[:,-1]
  avg_out=numpy.mean(y)
  arr4 = numpy.array(V)
  arr5=arr4.tolist()
  true_out=arr5[-1]
  error=error+(true_out-avg_out)**2
  j=j+1

Mean_sq = error/(len(val_set))
print(Mean_sq)

