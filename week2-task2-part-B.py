matrix = [] # This is the initial matrix.

print("Enter each row (numbers separated by the spaces).")
print("Press the enter on blank line to finish.")

while True:
    user_input = [int(x) for x in input().split()]

    if(user_input == []):
        break

    matrix.append(user_input)

n = len(matrix) # This is the number of rows and column as both are same here.
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

# This loop is to find the primary diagonal sum
for i in range(n):  
    primary_diagonal_sum = primary_diagonal_sum + matrix[i][i]

# To find Seconday diagonal sum
for i in range(n):
    secondary_diagonal_sum = secondary_diagonal_sum + matrix[i][n-i-1]

print(f"Primary Diagonal Sum = {primary_diagonal_sum}")
print(f"Secondary Digonal Sum = {secondary_diagonal_sum}")