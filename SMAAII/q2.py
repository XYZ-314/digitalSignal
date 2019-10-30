import numpy as np
import matplotlib.pyplot as plt
filename = 'wine/wine.data'
with open(filename) as f:
	dataset = f.readlines()
dataset = [line.replace('\n','').split(',') for line in dataset]
dataset = (np.array(dataset)).astype(float)
cov = np.cov(dataset.T[1:,:])
Eval, Evec = np.linalg.eig(cov)
fig = plt.figure()
eigen = fig.add_subplot(211)
project = fig.add_subplot(212)
plt.subplots_adjust(hspace = 1)
eigen.set_title('eigenvalues magnitude comparision')
eigen.set_xlabel('eigenvectors')
eigen.set_ylabel('eigenvalues')
project.set_xlim([-2000,0])
project.set_ylim([-1000,1000])
eigen.bar([i for i in range(1,14)],Eval,color = 'blue',width=0.5)
def plot_class(c,color):
	C = [x[1:] for x in dataset if x[0]==c]
	X = [np.dot(x,Evec[:,0]) for x in C]
	Y = [np.dot(x,Evec[:,1]) for x in C]
	project.scatter(X,Y,s=5.0,marker='o',color=color)
plot_class(1,'red')
plot_class(2,'black')
plot_class(3,'blue')
plt.legend(('class 1','class 2','color 3'))
plt.show()
