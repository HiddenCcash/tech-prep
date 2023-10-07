import collections

"""
Solution 2 Sliding Window
Does return the biggest package 
"""


def IDsOfPackages(truckSpace, packagesSpace):

    SAFTEY_SPACE_RESERVE = 30
    PACK_LENGTH = len(packagesSpace)
    GOAL_SPACE = truckSpace - SAFTEY_SPACE_RESERVE

    start = 0
    end = PACK_LENGTH - 1

    while start < end:
        package_sum = packagesSpace[start] + packageSpace[end]
        if package_sum == GOAL_SPACE:
            return [start, end]
        elif package_sum > GOAL_SPACE:
            end -= 1
        else:
            start += 1


truckSpace = 90
packageSpace = [1, 10, 25, 35, 60]
print(IDsOfPackages(truckSpace, packageSpace))
truckSpace = 90
packageSpace = [1, 10, 25, 35, 50, 60]
print(IDsOfPackages(truckSpace, packageSpace))  # ans = [1, 4]


"""
Solution 1 Hash table and complement
Does NOT return the pair with the biggest package
"""


def IDsOfPackages(truckSpace, packagesSpace):
    """
    A complement approach

    truckSpace : integer denotes max truck space
    packagesSpace : list of integers denoting space of package
    return : list of two packages denoted by integers representing their space
    """

    # init variables and constants
    SAFTEY_SPACE_RESERVE = 30
    PACK_LENGTH = len(packagesSpace)
    goalSpace = truckSpace - SAFTEY_SPACE_RESERVE
    packageMap = collections.defaultdict(int)
    pairs = []

    # loop through all possible packages
    for idx in range(PACK_LENGTH-1, -1, -1):
        packDiff = goalSpace - packagesSpace[idx]

        if packDiff in packageMap:
            # save pairs in order to select largest package if there is a tie
            return [idx, packageMap[packDiff]]

        packageMap[packagesSpace[idx]] = idx
        # packageSet.add(packagesSpace[idx])

    # sort and return package pair with the largest package space
    # return sorted(packageMap)


truckSpace = 90
packageSpace = [1, 10, 25, 35, 60]
print(IDsOfPackages(truckSpace, packageSpace))
truckSpace = 90
packageSpace = [1, 10, 25, 35, 50, 60]
print(IDsOfPackages(truckSpace, packageSpace))  # ans = [1, 4]
