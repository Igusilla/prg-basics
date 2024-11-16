def convert_to_1d(array_2d):
    """Convert a 2D array into a 1D array."""
    return [element for row in array_2d for element in row]

def print_1d_array(array_2d):
    """Print a 1D array converted from a 2D array."""
    array_1d = convert_to_1d(array_2d)
    print("Original 2D Array:")
    for row in array_2d:
        print(row)
    print("Converted 1D Array:")
    print(array_1d)
    print()

# Example 2D Arrays
array1 = [
    [2, 3],
    [1, 5]
]

array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2],
]

array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Print results
print_1d_array(array1)
print_1d_array(array2)
print_1d_array(array3)