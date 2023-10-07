"""
You are given a 2D list of lists.
There is at most one box denoted by zeros and all other elements are ones.
Return the ROI of the box
"""

# contains only box
grid1 = [[1, 1, 1, 1, 1],
         [0, 0, 1, 1, 1],
         [0, 0, 1, 1, 1]]
grid2 = [[1]]
grid3 = [[0]]
grid4 = [[1, 1, 1, 1, 1],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]]


def findROI(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            coords = {}
            if grid[row][col] == 0:
                coords['tl'] = (row, col)
                coords['br'] = (row, col)
                coords = searchDFS(row, col, grid, coords)
                return coords['tl'][0], coords['tl'][1], coords['br'][0], coords['br'][1]
    return None


def searchDFS(row, col, grid, coords):
    # check bounds
    if row < 0 or row > len(grid)-1:
        return
    if col < 0 or col > len(grid[0])-1:
        return
    # check if visited
    if grid[row][col] == 1:
        return

    # mark as visited
    grid[row][col] = 1

    # cache the possible bottom right coord
    if row+col > coords['br'][0]+coords['br'][1]:
        coords['br'] = (row, col)

    # continue to search nearest neighbors
    searchDFS(row-1, col, grid, coords)  # left
    searchDFS(row+1, col, grid, coords)  # right
    searchDFS(row, col+1, grid, coords)  # down
    searchDFS(row, col-1, grid, coords)  # up

    # if we reached this far, we have exhausted the DFS search
    return coords


print(findROI(grid1))
print(findROI(grid2))
print(findROI(grid3))
print(findROI(grid4))
