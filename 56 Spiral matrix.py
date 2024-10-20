matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

output = []
top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

while top <= bottom and left <= right:
    # Traverse from left to right across the top row
    for i in range(left, right + 1):
        output.append(matrix[top][i])
    top += 1

    # Traverse from top to bottom along the right column
    if top <= bottom:
        for i in range(top, bottom + 1):
            output.append(matrix[i][right])
        right -= 1

    # Traverse from right to left across the bottom row
    if top <= bottom:  # Ensure the row is still valid
        for i in range(right, left - 1, -1):
            output.append(matrix[bottom][i])
        bottom -= 1

    # Traverse from bottom to top along the left column
    if left <= right:  # Ensure the column is still valid
        for i in range(bottom, top - 1, -1):
            output.append(matrix[i][left])
        left += 1

print(output)
