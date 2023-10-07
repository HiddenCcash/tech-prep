"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9

https://leetcode.com/problems/prison-cells-after-n-days/solution/
"""

cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 1


def nextDay(cells, num_days, grid):
    if num_days == 0:
        # return cells[1:-1]
        return grid
    # argment cells must be padded with -2 on both ends
    nxt = [0]*len(cells)
    nxt[0] = nxt[-1] = -2

    for idx in range(1, len(cells)-1):
        neighbor_sum = cells[idx-1] + cells[idx+1]
        if neighbor_sum == 0 or neighbor_sum == 2:
            nxt[idx] = 1

    grid.append(nxt[1:-1])
    return nextDay(nxt, num_days-1, grid)

# FIXME: only works for less than 2^8 days


def findNDays(cells, N):

    # pad cells with -2 on each side
    grid = []
    grid.append(cells)
    cells.insert(0, -2)
    cells.append(-2)

    # determine grid length
    if N < 256:
        grid_length = N
        modulus = None
    else:
        grid_length = 256
        modulus = N % grid_length

    grid = nextDay(cells, grid_length, grid)

    if modulus != None:
        return grid[modulus]
    return grid[grid_length]


"""
[0, 1, 0, 0]

"""

cells = [0, 1, 0, 1, 1, 0, 0, 1]
print(findNDays(cells, N=1))
# cells = [0, 1, 0, 1, 1, 0, 0, 1]
# print(findNDays(cells, N=2))
# cells = [0, 1, 0, 1, 1, 0, 0, 1]
# print(findNDays(cells, N=3))
# cells = [0, 1, 0, 1, 1, 0, 0, 1]
# print(findNDays(cells, N=4))
# cells = [0, 1, 0, 1, 1, 0, 0, 1]
# cells = [0, 1, 1, 0, 1]
# print(findNDays(cells, N=1000000000))


"""
Solution

"""


class Solution(object):
    def prisonAfterNDays(self, cells, N):
        def nextday(cells):
            return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1])
                    for i in xrange(8)]

        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                # N %= seen[c] - N
                # Calculate the time period: seen[c] - N b/c that is
                # the diff between the first time seeing c at day N and the current N day.
                # I.e., we have found a moment where it starts repeats so now we can jump
                # ahead to a new N by getting the remainder of the current N day
                # divided by the time period
                N = N % (seen[c] - N)
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = nextday(cells)

        return cells
