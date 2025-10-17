"""
Problem:
In the previous exercise, you wrote a function that transposed a 3x3 matrix represented by 
a list of lists.

Matrix transposes are not limited to 3x3 matrices, or even square matrices. 
Any matrix can be transposed 
simply by switching columns with rows.

Modify your transpose function from the previous exercise so that it works 
with any MxN matrix with at least one row and one column.


input: MxN matrix
ouput: transposed matrix

rules:
    explicit:
    - same as previous exercise but should work with any M x N matrix
    implicit:
    - expect valid input

datastructure:
nested list

algorithm:
use zip solution
1.) 
"""

def transpose(matrix):
    zipped = zip(*matrix)
    return [list(row) for row in zipped]

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)

def transpose2(matrix):
    new = [[] for _ in range(len(matrix[0]))]
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            new[col_idx].append(matrix[row_idx][col_idx])
    return new

# All of these examples should print True
print(transpose2([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose2([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose2([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose2(matrix_3_by_5) == expected_result)