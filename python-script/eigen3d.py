import numpy as np
first = input("first equation here: ")
second = input("second equation here: ")
third = input("third equation here: ")
print(first,second,third)
matrix = first+";"+second+";"+third
A = np.mat(matrix)
print(A)
eigenvalues = np.linalg.eigvals(A)
print("lambda = "+ str(eigenvalues))