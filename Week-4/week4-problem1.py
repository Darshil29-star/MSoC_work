import pandas as pd

data = {
    'Name' : ['Alice' , 'Bob' , 'Charlie', 'David'],
    'Age' : [21,19,22,20],
    'City' : ['Delhi' , 'Mumbai' , 'Ahmedabad' , 'Pune']  
}

df = pd.DataFrame(data) # Task-1

print(df.head(2))  # Task-2

print(df.columns)  #Task-3

print(df.shape)    #Task-4  ans:(4,3)  as it contains 4 rows and 3 columns.

print(df.info())   # Task-5  to get the infomation about the dataframe.
