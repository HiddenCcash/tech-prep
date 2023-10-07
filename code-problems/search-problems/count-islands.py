"""
Given a 2D grid, count the number of islands, where 1 denotes island and 0 denotes
water. Islands can be connected in cardinal directions (up, down, left, right).
Return the number of islands
"""

# one island
grid = [[0, 0, 0],
        [0, 1, 1],
        [0, 0, 1]]
# two islands
grid2 = [[0, 0, 0],
         [0, 1, 1],
         [1, 0, 1]]
#  one island
grid3 = [[0, 0, 1],
         [1, 1, 1],
         [1, 0, 1]]
#  zero islands
grid4 = [[0]]
# one island
grid5 = [[1]]

grid6 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]]

"""DFS"""


def countIslandDFS(grid):
    if not len(grid):
        return 0
    cnt = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                search(row, col, grid)
                cnt += 1
    return cnt


def search(row, col, grid):
    # check bounds
    if row < 0 or row > len(grid)-1:
        return
    if col < 0 or col > len(grid[0])-1:
        return
    if grid[row][col] == 0:
        return
    # mark as visited
    grid[row][col] = 0
    # explore new land depth first
    search(row-1, col, grid)  # up
    search(row+1, col, grid)  # down
    search(row, col-1, grid)  # left
    search(row, col+1, grid)  # right


"""BFS"""


def countIslandBFS(grid):
    if not len(grid):
        return 0
    cnt = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                serachBFS(row, col, grid)
                cnt += 1
    return cnt


def serachBFS(row, col, grid):
    # add to queue
    queue = []
    queue.append((row, col))
    while(len(queue) > 0):
        # get first node
        row, col = queue.pop(0)
        # mark as visited
        grid[row][col] = 0

        # up
        if isLand(row-1, col, grid):
            queue.append((row-1, col))
        # down
        if isLand(row+1, col, grid):
            queue.append((row+1, col))
        # left
        if isLand(row, col-1, grid):
            queue.append((row, col-1))
        # right
        if isLand(row, col+1, grid):
            queue.append((row, col+1))


def isLand(row, col, grid):
    # check bounds
    if row < 0 or row > len(grid)-1:
        return False
    if col < 0 or col > len(grid[0])-1:
        return False
    # check if land
    if grid[row][col]:
        return True


# assert countIslandDFS(grid) == 1
# assert countIslandDFS(grid2) == 2
# assert countIslandDFS(grid3) == 1
# assert countIslandDFS(grid4) == 0
# assert countIslandDFS(grid5) == 1
assert countIslandBFS(grid) == 1
assert countIslandBFS(grid2) == 2
assert countIslandBFS(grid3) == 1
assert countIslandBFS(grid4) == 0
assert countIslandBFS(grid5) == 1
