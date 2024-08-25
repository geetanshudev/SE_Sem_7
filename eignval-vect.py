import numpy as np 
from numpy import linalg

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a)

b,c = linalg.eigh(a)

print("Eigen values are : ",b)
print("Eigen Vectors are : ",c)
