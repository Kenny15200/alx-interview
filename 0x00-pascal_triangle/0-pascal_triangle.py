#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        row = [1]  # The first element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            # Generate the next row based on the previous row
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)  # The last element in each row is always 1
        triangle.append(row)
    
    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)

