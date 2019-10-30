import numpy as np
import matplotlib.pyplot as plt

with open('wine/wine.data') as fi:
    data = fi.readlines()

data = [x.replace('\n','').split(',') for x in data]
data = (np.array(data)).astype(float)

eigenval, eigenvec = np.linalg.eig(np.cov(data.T[1:,:]))

fig = plt.figure()

eigen_plot = fig.add_subplot(121)
p2_plot = fig.add_subplot(122)

plt.subplots_adjust(hspace=1)
eigen_plot.set_title('part 1')
eigen_plot.set_xlabel('EigenVector')
eigen_plot.set_ylabel('EigenValue')

p2_plot.set_xlim([-1500,0])
p2_plot.set_ylim([-1000,1000])
eigen_plot.bar([i for i in range(1,14)],eigenval,width=0.5)

def fun(c,co):
    C = [x[1:] for x in data if x[0] == c]
    X = [np.dot(x,eigenvec[:,0]) for x in C]
    Y = [np.dot(x,eigenvec[:,1]) for x in C]
    p2_plot.scatter(X,Y,marker='x',color = co)

fun(1,'red')                    
fun(2,'black')
fun(3,'blue')
plt.legend(('class 1','class 2','class 3'))
plt.show()
 

