matrix = [] # This is the initial matrix.

print("Enter each row (numbers separated by the spaces).")
print("Press the enter on blank line to finish.")

while True:
    user_input = [int(x) for x in input().split()]

    if(user_input == []):
        break

    matrix.append(user_input)

row = len(matrix)
column = len(matrix[0])

final_matrix = []   # This is the transpose of initial matrix.
for c in range(column):
    current_row = []
    for r in range(row):
        current_row.append(matrix[r][c])
    final_matrix.append(current_row)
print(final_matrix)