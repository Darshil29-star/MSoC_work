import numpy as np

marks = np.array([[80,90,70] , [50,60,70] , [90,95,85]])

row_mean = []
for row in marks:
    row_mean.append(np.mean(row))

row_mean = np.array(row_mean)
req_ind = [i for i,val in enumerate(row_mean) if(val > 75)]

print(req_ind)