import pandas as pd

data = pd.read_csv("Cleaned_data.csv")

# print(data.columns)
female_passengers = data[data['Sex'] == 'female']  # Task-1 to find all the female passsengers from this dataset.
# print(female_passengers)

older_30 = data[data['Age'] > 30]  # Task-2 to get all the passengerrs which are older than 30 years.
# print(older_30['Age'])

survived_passeengers = data[data['Survived'] == 1]  # Task-3 to get the survived passengers from the dataset.
# print(survived_passeengers['Survived'])

female_survived = data[(data['Sex'] == 'female') & (data['Survived'] == 1)]  # Task-4 to get the female passengers who survived.
# print(female_survived[['Sex' , 'Survived']])

average_age = data['Age'].mean()  # Task-5 to get the average age of all passengers.
# print(average_age)

print(data.loc[data['Age'].idxmax()])  # Task-6 to get the detail about the oldest person from the dataset.
