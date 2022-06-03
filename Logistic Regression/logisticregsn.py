from sklearn import datasets
import numpy as np
import random
import matplotlib.pyplot as plt
import math

iris = datasets.load_iris()
x = iris.data[:, :2]
y = (iris.target != 0) * 1

x = np.insert(x, 2, y, axis=1)
random.shuffle(x)

data = x.tolist()
train_set = []
val_set = []
test_set = []

for x1 in data:
    R = random.uniform(0, 1)
    if R >= 0 and R <= 0.7:
        train_set.append(x1)
    elif R > 0.7 and R <= 0.85:
        val_set.append(x1)
    else:
        test_set.append(x1)

aa = np.array(train_set)
aa = np.insert(aa, 0, 1, axis=1)

theta = np.random.rand(3)

train_loss = []
lr = 0.00001
for i in range(1000):
    k = 0
    TJ = 0
    for T in train_set:
        xx = np.array(aa[k, :-1])

        z = np.dot(xx, theta)

        h = 1 / (1 + np.exp(-z))
        k = k + 1
        yy = T[-1]
        j = -yy * math.log(h) - (1 - yy) * math.log(1 - h)

        TJ = TJ + j
        dv = xx * (h - yy)
        theta = theta - dv * lr
    TJ = TJ / len(train_set)
    train_loss.append(TJ)
xy = []
for a in range(1000):
    xy.append(a)

plt.plot(xy, train_loss)
plt.show()

bb = np.array(val_set)
bb = np.insert(bb, 0, 1, axis=1)
kk = 0
correct = 0

for b in val_set:
    xx = np.array(bb[kk, :-1])
    z = np.dot(xx, theta)
    h = 1 / (1 + np.exp(-z))

    if h >= 0.5:
        h = 1
    else:
        h = 0

    yyy = b[-1]
    if yyy == h:
        correct = correct + 1

    kk = kk + 1
val_acc = (correct / len(val_set)) * 100

print(val_acc)