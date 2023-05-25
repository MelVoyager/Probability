import numpy as np

# 假设我们有一个2x2矩阵
A = np.array([[0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]])

# A = A.T
# 使用numpy.linalg.eig()函数计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

print("矩阵：\n", A)
print("特征值：\n", eigenvalues)
print("特征向量：\n", eigenvectors)

print(np.matmul(A, eigenvectors[0]))