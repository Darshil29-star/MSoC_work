import numpy as np

def risk_score(amount , timespent , failedattempts):
    result = (0.6*amount) + (0.3*timespent) + (0.1*failedattempts)
    return result

trans = np.array([[1000,50,0] , [5000,20,2] , [3000,80,5]])
normalized_trans = (trans - trans.min(axis=0))/(trans.max(axis=0) - trans.min(axis=0))  # This is to normalize our given data .i.e to scale the given data in small values.
k = 2

risky_scores = []
for row in normalized_trans:
    risky_scores.append(risk_score(row[0] , row[1] , row[2]))

top_k_risky_users = sorted(range(len(risky_scores)) , key = lambda i:risky_scores[i], reverse=True)[:k]  # After this step we will get out desired result   I have search this method in google as I have no idea about it.

print(top_k_risky_users)