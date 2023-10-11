#!/usr/bin/python3

def pascal_triangle(n):
    # Check if n is a positive integer
    if n <= 0 or not isinstance(n, int):
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate the rest of the rows
    for i in range(1, n):
        # Calculate the next row
        previous_row = triangle[-1]
        new_row = [1]  # First element is always 1
        for j in range(1, i):
            new_value = previous_row[j - 1] + previous_row[j]
            new_row.append(new_value)
        new_row.append(1)  # Last element is always 1

        # Append the new row to the triangle
        triangle.append(new_row)

    return triangle

# Example usage:
if __name__ == "__main__":
    result = pascal_triangle(5)
    for row in result:
        print(row)

