import numpy as np

arr = np.array([[1,2,3] , [5,5,5] , [2,2,2]]) # given array.

row_sum = []  # Empty list to store the sum of all the rows.
for row in arr:
    row_sum.append(np.sum(row))  # adding the sum of each row in out empty list.

index = row_sum.index(max(row_sum)) # finding the index of maximum element i.e. maximum sum.
print(index)