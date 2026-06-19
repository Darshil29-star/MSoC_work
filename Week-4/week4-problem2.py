import pandas as pd

data = {
    'Product' : ['Laptop' , 'Mouse' , 'Keyboard' , 'Monitor'],
    'Price' : [50000,500,1500,12000],
    'Quantity' : [5,20,15,7]
}

df = pd.DataFrame(data)

print(df['Product'])    # Task-1 selecting the product columns only.

print(df[['Product' , 'Price']])    # Task-2 selecting 2 specific columns.

print(df[df['Price'] > 1000]['Product'])  # Task-3 to get the list of product whose price is greater than 1000.

print(df[df['Quantity'] < 10]['Product'])   # Task-4 to get the list of product whose quantity is less than 10.

print(df[(df['Price'] > 1000) & (df['Quantity'] < 10)]['Product'])  # Task-5 to get the list of product which satisfy both the above conditions.
