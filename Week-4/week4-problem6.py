import pandas as pd

data = pd.read_csv("Cleaned_data.csv")

survival_rate = data.groupby('Sex')['Survived'].mean()  # Task-1 to get the survival rate groupby the gender.
# print(survival_rate)

# print(data.columns)
average_age_passenger_class = data.groupby('Pclass')['Age'].mean()  # Task-2 to find the average age groupby the passenger class.
# print(average_age_passenger_class)

number_of_passenger_each_class = data['Pclass'].value_counts()  # Task-3 to get the number of passengers in each class.
# print(number_of_passenger_each_class)

survival_rate_class = data.groupby('Pclass')['Survived'].mean()  # Task-4 to get the class with maximum survial rate.
# print(survival_rate_class.idxmax())  # This will display number of class which has maximum survival rate.

average_fair_each_class = data.groupby('Pclass')['Fare'].mean()  # Task-5 to get the average fair of each class.
print(average_fair_each_class)

