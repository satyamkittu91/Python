import numpy as np
 
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype='int64')

print(a)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

print(a.shape)  # (3, 3)
print(a.ndim)   # 2
print(a.dtype)  # int64
print(a.size)   # 9
print(a.itemsize)  # 8 (bytes per element)
print(a.nbytes)  # 72 (total bytes of the array)
print(a.T)  # Transpose of the array
print(a.T.shape)  # (3, 3)

# Get a specific element
print(a[0, 1])  # 2 (first row, second column)
print(a[1, 2])  # 6 (second row, third column)
print(a[2, 0])  # 7 (third row, first column)

# Get a specific row
print(a[1])  # [4 5 6] (second row)
print(a[1, :])  # [4 5 6] (second row, all columns)

# Get a specific column
print(a[:, 1])  # [2 5 8] (all rows, second column)
print(a[:, 2])  # [3 6 9] (all rows, third column)

# [starring:ending:step]
print(a[::2, ::2])  # [[1 3] [7 9]] (every second row and column)

# We can modify each element of the array
# a[0, 0] = 10  # This will change the first element to 10
# print(a)  # [[10 2 3] [4 5 6] [7 8 9]]

# Initiliazing Different Types of Arrays

# All 0s matrix
print(np.zeros((2, 3)))  # 2 rows, 3 columns
# [[0. 0. 0.] 
# [0. 0. 0.]]

# All 1s matrix
print(np.ones((2, 3)))  # 2 rows, 3 columns
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Any other number
print(np.full((2, 3), 7))  # 2 rows, 3 columns, filled with 7
# [[7 7 7]
#  [7 7 7]]


# Random decimal numbers
print(np.random.rand(2, 3))  # 2 rows, 3 columns
# [[0.5488135  0.71518937 0.60276338]
#  [0.54488318 0.4236548  0.64589411]]
# or any different number
print(np.random.random_sample(a.shape))  # 2 rows, 3 columns
'''
[[0.33470802 0.35097933 0.88173268]
 [0.33747832 0.0185629  0.65991463]
 [0.25785934 0.21383168 0.96764294]]
'''
# Random integer values
print(np.random.randint(0, 10, (2, 3)))  # 2 rows, 3 columns, random integers between 0 and 10
# [[5 1 2]
#  [7 4 8]]
# or any different number

# Identity Matrix
print(np.identity(3))  # 3x3 identity matrix
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

r1 = np.repeat(a, 3, axis=0)  # Repeat each row 3 times
'''
[[1 2 3]
 [1 2 3]
 [1 2 3]
 [4 5 6]
 [4 5 6]
 [4 5 6]
 [7 8 9]
 [7 8 9]
 [7 8 9]]
'''
r2 = np.repeat(a, 3, axis=1)  # Repeat each column 3 times
'''
[[1 1 1 2 2 2 3 3 3]
 [4 4 4 5 5 5 6 6 6]
 [7 7 7 8 8 8 9 9 9]]
'''

# Mathematics
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a + 2)  # Add 2 to each element
print(a - 2)  # Subtract 2 from each element
print(a * 2)  # Multiply each element by 2
print(a / 2)  # Divide each element by 2
print(a ** 2)  # Square each element

print(a + b)  # Element-wise addition
print(a - b)  # Element-wise subtraction
print(a * b)  # Element-wise multiplication
print(a / b)  # Element-wise division
print(a ** b)  # Element-wise exponentiation
print(np.add(a, b))  # Element-wise addition using numpy function

# Linear Algebra
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.matmul(a, b)  # Matrix multiplication
np.add(a, b)  # Matrix addition
np.subtract(a, b)  # Matrix subtraction


#Statistics
np.min(a)  # Minimum value in the array
np.max(a)  # Maximum value in the array
np.sum(a)  # Sum of all elements in the array
np.min(a, axis=0)  # Minimum value in each column
np.min(a, axis=1)  # Minimum value in each row
np.max(a, axis=0)  # Maximum value in each column
np.max(a, axis=1)  # Maximum value in each row

# Reorganizing Arrays
np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).reshape(1, 9)  # Reshape to 1 row and 9 columns 
# [[1 2 3 4 5 6 7 8 9]]
np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).reshape(9, 1)  # Reshape to 9 rows and 1 column 
'''
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]
 [9]]
'''

 # Vertically stacking arrays
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
c = np.vstack((a, b))  # Stack arrays vertically
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Horizontal Stack
print(np.hstack((a, b))) # Stack arrays Horizontally
'''
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
'''

#load data from file
# filedata = np.genfromtxt('data.txt', delimiter=',')


# Broadcasting
a = np.array([[1, 2, 3]])
b = np.array([[4], [5], [6]])

print(a+b)
# [[5 6 7]
#  [6 7 8]
#  [7 8 9]]
# Broadcasting allows numpy to perform operations on arrays of different shapes

# dot product
np.dot(a, b)  # Dot product of two arrays
# [[32]] (1x3 dot 3x1 = 1x1)
# or using @ operator

np.argmax(a)  # Index of the maximum value in the array
np.argmin(a)  # Index of the minimum value in the array
np.argsort(a)  # Indices that would sort the array
np.where(a > 2)  # Indices of elements that satisfy the condition

# Boolean Masking
a = np.array([1, 2, 3, 4, 5])
mask = a > 3
print(a[mask]) # [4 5]
# or directly
print(a[a > 3]) # [4 5]

# Axis Operations
a = np.array([[1, 2], [3, 4]])
print(np.sum(a, axis=0)) # column-wise sum: [4 6]
print(np.sum(a, axis=1)) # row-wise sum: [3 7]
