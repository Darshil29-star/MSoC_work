import pandas as pd

data = {
    'Student' : ['A','B','C','D'],
    'Maths' : [85,70,95,60],
    'Science' : [90,65,88,75]
}

df = pd.DataFrame(data)

df['Total'] = df['Maths']+df['Science']   # Task-1  to create column total.
# print(df)

df['Average'] = df['Total']/2   # Task-2  to create a column average.
# print(df)

print(df.loc[df['Total'].idxmax()])  # Task-3  to get the detail of student who have maximum total of marks.

df = df.sort_values(by='Average' , ascending=False)  # Task-4  to sort the dataframe by average value in decreasing order.
# print(df)

print(df[df['Average'] > 80])  # Task-5  to get the students whose average is greater than 80.