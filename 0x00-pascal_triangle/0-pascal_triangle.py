#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for _ in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # The first element is always 1
        for i in range(1, len(prev_row)):
            new_value = prev_row[i - 1] + prev_row[i]  # Calculate new values
            new_row.append(new_value)
        new_row.append(1)  # The last element is always 1
        triangle.append(new_row)

    return triangle

# Example usage:
if __name__ == "__main__":
    n = 5
    result = pascal_triangle(n)
    for row in result:
        print(row)

