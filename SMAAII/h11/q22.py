from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt


def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    num_points = len(lines)
    dim_points = 28 * 28
    data = np.empty((num_points, dim_points))
    labels = np.empty(num_points)

    for ind, line in enumerate(lines):
        num = line.split(',')
        labels[ind] = int(num[0])
        data[ind] = [int(x) for x in num[1:]]

    return (data, labels)


train_data, train_labels = read_data("sample_train.csv")
test_data, test_labels = read_data("sample_test.csv")

# PCA

dataM = train_data
dataM = dataM - np.mean(dataM, axis=0)
eig_val, eig_vect = np.linalg.eig(np.cov(dataM.T))
# taking first 2 eigen vectors corresponding to 2 highest eigen values
eig_vect = eig_vect[:, 0:2]
dataProjPCA = dataM@eig_vect


# Gradient Descent
wei = np.random.rand(dataM.shape[1], 2)
wei, o, p = np.linalg.svd(wei)
wei = wei[:, :2]


def gradient(V):
    transdata = np.transpose(dataM)
    transV = np.transpose(V)
    PP = dataM@V@transV - dataM
    ZZ = V@transV@transdata - transdata
    return ((transdata@(PP)@V)/np.linalg.norm(PP)) + ((ZZ@dataM@V)/np.linalg.norm(ZZ))


for _ in range(100):
    up = 0.00001*gradient(wei)
    wei = wei + up

dataProjGD = dataM@wei

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Normal Pca')
plt.scatter(dataProjPCA[:, 0:1], dataProjPCA[:, 1: 2])
plt.show()

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Gradient Descent Pca')
plt.scatter(-dataProjGD[:, 0: 1], dataProjGD[:, 1: 2])
plt.show()
