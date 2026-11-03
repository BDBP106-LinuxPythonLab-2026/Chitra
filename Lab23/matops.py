import numpy as np
def dot_product(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if a.ndim != 1 or b.ndim != 1 or a.size != b.size:
        print("Error: vectors must be 1D and have equal lengths")
        return None
    return np.dot(a, b)
def matrix_vector_product(A, v):
    A, v = np.asarray(A), np.asarray(v)
    if A.ndim != 2 or v.ndim != 1 or A.shape[1] != v.size:
        print("Error: number of matrix columns must equal vector length")
        return None
    return np.dot(A, v)
def matrix_matrix_product(A, B):
    A, B = np.asarray(A), np.asarray(B)
    if A.ndim != 2 or B.ndim != 2 or A.shape[1] != B.shape[0]:
        print("Error: columns of first matrix must equal rows of second")
        return None
    return np.dot(A, B)
def cross_product(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if a.ndim != 1 or b.ndim != 1 or a.size != 3 or b.size != 3:
        print("Error: cross product requires two 3D vectors")
        return None
    return np.cross(a, b)
a=np.array([1,2,3])
b=np.array([4,5,6])
A=np.array([[1,2,3],[4,5,6]])
B=np.array([[1,2],[3,4],[5,6]])
print(dot_product(a,b))
print(cross_product(a,b))
print(matrix_vector_product(a,b))
print(matrix_matrix_product(a,b))