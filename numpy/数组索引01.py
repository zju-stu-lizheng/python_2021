import numpy as np

# Create the following rank 2 array with shape(3,4)
# [[1,2,3,4],
#  [5,6,7,8],
#  [9,10,11,12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

'''
# Using slicing to pull out subarray consisting of the first 2 rows
# and columns 1 and 2;b is the following array of shape(2,2)
# [[2,3]
#  [6,7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data ,so modifyig
# it will modify the original array
print(a[0,1])
b[0,0] = 77  # b[0,0] is the same piece of data as a[0,1]
print(a[0,1])
'''

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1,:]     # Rank 1 view of the second row of a
row_r2 = a[1:2,:]   # Rank 2 view of the second row of a
print(row_r1,row_r1.shape)  # [5 6 7 8] (4,)
print(row_r2,row_r2.shape)  # [[5 6 7 8]] (1, 4)

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]    # Rank 1 view of the second column of a
col_r2 = a[:, 1:2]  # Rank 2 view of the second column of a
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Prints "[[ 2]
                             #          [ 6]
                             #          [10]] (3, 1)"
