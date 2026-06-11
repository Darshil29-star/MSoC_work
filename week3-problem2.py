# This include the code to print the even number only from a given array.
import numpy as np

arr = np.array([1,2,3,4,5,6])

even_arr = arr[arr%2 == 0]  # using the boolean indexing to find only those elements which are even.
print(even_arr)