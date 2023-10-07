"""
Using list comprehension, create a 2D matrix of 0's
"""

COLS = 3
ROWS = 5

# In what order does this execute? Left to right? or Right to Left?
# It actually executes from inner to outer
# Is it a 3x5 or 5x3 matrix (where row x height)
matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

for row in matrix:
    print(row)
print()

"""
Create a list of lists in the shape of a pyramid
[
[0],
[0, 1],
[0, 1, 2],
[0, 1, 2, 3]
]
"""

ROWS = 10
matrix = [[num for num in range(_num)] for _num in range(1, ROWS+1)]

for row in matrix:
    print(row)
print()

# Upside down
ROWS = 10
matrix = [[num for num in range(_num)] for _num in range(ROWS, -1, -1)]

for row in matrix:
    print(row)
print()


"""
Initialize the first row and the first colum with an indexing like so
[0, 1, 2]
[1, 0, 0]
[2, 0, 0]
[3, 0, 0]
[4, 0, 0]
"""
COLS = 10
ROWS = 5
matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# index the entire first colum
for row_i in range(ROWS):
    matrix[row_i][0] = row_i

# index the entire first row
for col_i in range(COLS):
    matrix[0][col_i] = col_i

for row in matrix:
    print(row)

foo = [child for child in (1, 2)]
print(foo)

# this slicing foo[-2::-1] first
# first slices the list with foo[-2:] ==> [1, 2, 3, 4, 5, 6]
# second, reverses the list ==> [6, 5, 4, 3, 2, 1]
foo = [1, 2, 3, 4, 5, 6, 7]
print('foo[-3:]', foo[-2::-1])
