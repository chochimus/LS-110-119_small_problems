"""
Problem:
A 3x3 matrix can be represented by a list of nested lists: 
an outer list that contains three sub-lists that each contain three elements.
 For example, the 3x3 matrix shown below:

Copy Code
1  5  8
4  7  2
3  9  6
is represented by the following list of lists:

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

The transpose of a 3x3 matrix is the matrix that results from exchanging the 
rows and columns of the original matrix. For example, the transposition of the 
matrix shown above is:


1  4  3
5  7  9
8  2  6
Write a function that takes a list of lists that represents a 3x3 
matrix and returns the transpose of the matrix. You should implement the 
function on your own, without using any external libraries.

Take care not to modify the original matrix -- your function must produce 
a new matrix and leave the input matrix list unchanged.


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

input: 2d list matrix
output: 2d list transposed matrix

rules:
    explicit:
    - matrix is a 3x3 nested list
    - transpose is columns swapped with rows
    - should produce a new matrix
    implicit:
    - expect good input

datastructure:
nested list

algorithm:
1.) zip rows
2.) convert zipped tuples into lists
3.) return new object
"""

def transpose(matrix):
    r1,r2,r3 = matrix
    zipped = zip(r1,r2,r3)
    return [list(row) for row in zipped]

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

def transpose2(matrix): #non-zip solution
    new = [[] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new[j].append(matrix[i][j])
    return new

new_matrix = transpose2(matrix)
print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True