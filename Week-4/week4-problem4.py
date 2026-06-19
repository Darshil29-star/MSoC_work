import pandas as pd

data = pd.read_csv('Titanic-Dataset.csv')  # Task-1 to load the dataset using the pandas.
# print(data)

# print(data.head(10))  # Task-2 to display the first 10 rows of the dataset.

# print(data.info())  # Task-3 to get the information about the rows and columns.

# print(data.columns)  # Task-4 to display all the columns name.

# print(data.isna().sum())  # Task-5 to get the missing values in each columns.
data = data.dropna()  # Currently I am dropping all the missing values in this dataset.

# print(data.describe())

data.to_csv("Cleaned_data.csv" , index=False)