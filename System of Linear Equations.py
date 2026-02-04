#Program to find the solution for the given linear equations.
#Developed by:keerthana k
#RegisterNumber:212225230137
import numpy as np

matrixA= np.array([[1,-3],[3,1]])

B= np.array([0,10])
result= np.linalg.solve(matrixA,B)

print(result)
