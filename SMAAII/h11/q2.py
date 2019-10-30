#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


X, train_labels = read_data("sample_train.csv")
test_data, test_labels = read_data("sample_test.csv")
X = X-np.mean(X, axis=0)
print(X.shape, test_data.shape)
print(train_labels.shape, test_labels.shape)


# In[2]:


cov_mat = np.cov(X.T)
eigen_values, eigen_vectors = np.linalg.eig(cov_mat)
eigen_vectors = eigen_vectors[:, 0:2]
X_con = X@eigen_vectors


# In[3]:


def diffren_f(Z):
    A = X@Z@Z.T-X
    B = Z@Z.T@X.T+(-X).T
    Ans = (X.T@A@Z)/np.linalg.norm(A)-(B@X@Z)/np.linalg.norm(B)
    return Ans


# In[4]:


d = X.shape[1]
w = np.random.rand(d, 2)
w, _, _ = np.linalg.svd(w)
w = w[:, :2]
q = 100
learning_rate = 1e-5
print(w.shape)
while q > 0:
    q -= 1
    wcon = w+learning_rate*diffren_f(w)
    err = X@w@w.T-X
    print("error=", np.linalg.norm(err))
    w = wcon


# In[5]:


plt.scatter(X_con[:, 0:1], X_con[:, 1:2])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Normal Pca')
plt.show()
X1_con = X@w
plt.scatter(-X1_con[:, 0:1], X1_con[:, 1:2])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('GD Pca')
plt.show()
