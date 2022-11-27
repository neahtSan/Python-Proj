import numpy as np
first = input("first equation here: ")
second = input("second equation here: ")
print(first,second)
matrix = first+";"+second
A = np.mat(matrix)
print(A)
eigenvalues = np.linalg.eigvals(A)
print("lambda = "+ str(eigenvalues))
