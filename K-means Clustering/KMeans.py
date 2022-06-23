from google.colab import drive

drive.mount('/content/gdrive')

from numpy import genfromtxt

data_path = '/content/gdrive/MyDrive/AI/centers.csv'
cntr = genfromtxt(data_path, delimiter=',')

data_path2 = '/content/gdrive/MyDrive/AI/data.csv'
data = genfromtxt(data_path2, delimiter=',')

cntr2 = cntr.tolist()

data2 = data.tolist()

cluster = []
cluster.append([])
cluster.append([])
cluster.append([])
cluster.append([])
cluster.append([])
cluster.append([])

import numpy

itr = 0
while True:

    temp_cluster = []
    temp_cluster.append([])
    temp_cluster.append([])
    temp_cluster.append([])
    temp_cluster.append([])
    temp_cluster.append([])
    temp_cluster.append([])

    i = 0
    for S in data2:
        j = 0
        distance = []
        for C in cntr2:
            a2 = numpy.array(data[i])
            a3 = numpy.array(cntr[j])
            dist = numpy.linalg.norm(a2 - a3)
            distance.append(dist)
            j = j + 1
        min_index = distance.index(min(distance))

        temp_cluster[min_index].append(i)

        i = i + 1

    k = 0
    for xx in temp_cluster:
        zz = data[xx]
        column_mean = numpy.mean(zz, axis=0)
        column1_mean = column_mean[0]
        column2_mean = column_mean[1]

        cntr[k, 0] = column1_mean
        cntr[k, 1] = column2_mean

        k = k + 1
    itr = itr + 1
    if itr > 1:
        ij = 0
        shift = 0
        for sm in data:
            ab = data[ij]

            abc = ab.tolist()
            ix = 0

            for xy in temp_cluster:
                d = data[xy]
                if abc in d.tolist():
                    break
                ix = ix + 1

            iz = 0
            for xz in cluster:
                dd = data[xz]
                if abc in dd.tolist():
                    break
                iz = iz + 1
            if ix != iz:
                shift = shift + 1
            ij = ij + 1
        if shift < 10:
            cluster = temp_cluster
            break
    cluster = temp_cluster

import matplotlib.pyplot as plt

for yy in cluster:
    zx = data[yy]

    plt.scatter(zx[:, 0], zx[:, 1])
plt.scatter(cntr[:, 0], cntr[:, 1], c='black')

plt.show()


