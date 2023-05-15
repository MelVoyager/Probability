import numpy as np

a = [1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1]
c = [[0, 0], [0, 0]]
for i in range(len(a) - 1):
    c[a[i]][a[i+1]] = c[a[i]][a[i+1]] + 1
    
M = np.array([[2/9, 7/9], [1/2, 1/2]])
X0 = np.array([1, 0])
# print(X0)
X1 = X0.dot(M)
X2 = X1.dot(M)
X3 = X2.dot(M)
print(X3)