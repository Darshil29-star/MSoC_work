# This code includes the code finding the sum, mean and maximum element from the array.
import numpy as np

arr = np.array([1,2,3,4,5])

arr_sum = np.sum(arr) # to find the sum of all the elements of array.
arr_mean = np.mean(arr) # to find the mean of all the elements of array.
arr_max = np.max(arr) # to find the maximum element among all the elements of the array.

print(f"Sum = {arr_sum}")
print(f"Mean = {arr_mean}")
print(f"Max = {arr_max}")
