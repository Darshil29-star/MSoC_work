import numpy as np

traffic = np.array([[100,120,110] , [90,95,100] , [500,550,600]])  # Here each row represent the individual server .

traffic_mean = np.mean(traffic)  # to find the universal mean of the given array.
servers_avg = np.mean(traffic , axis=1)

req_index = np.where(servers_avg > 2*traffic_mean)[0]
final = req_index.tolist()
print(final)
# print(type(final))