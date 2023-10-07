import collections
import heapq

maxTravelDist = 10000
forwards = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
returns = [[1, 2000], [2, 3000], [3, 4000], 4, [5000]]
# ans = [[2, 4], [3, 2]]

"""
Solution 2 - min-heap with grid construction
Runtime = f * r * log(f*r)

real    0m0.035s
user    0m0.016s
sys     0m0.016s
"""


def findRoutePairs(maxTravelDist, forwards, returns):

    routes = []
    bestRoutes = []
    for forward in forwards:
        for back in returns:
            distance = forward[1] + back[1]
            if distance <= maxTravelDist:
                heapq.heappush(routes, (-distance, [forward[0], back[0]]))

    if len(routes) == 0:
        return []

    bestRoute = heapq.heappop(routes)
    bestRoutes.append(bestRoute[1])
    while len(routes) > 0:
        nextBestRoute = heapq.heappop(routes)
        # if the next best route distance is less than the best route distance then break
        # note that both values are negative
        if nextBestRoute[0] > bestRoute[0]:
            break
        bestRoutes.append(nextBestRoute[1])

    return bestRoutes


maxTravelDist = 10000
forwards = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
returns = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
print(findRoutePairs(maxTravelDist, forwards, returns))


"""
Solution 1 - sorting

real    0m0.035s
user    0m0.016s
sys     0m0.016s
"""


def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):

    # NOTE: output will always be a list of pair-lists, one forward and one return
    routeMap = collections.defaultdict(int)

    for fRoute in forwardRouteList:
        for rRoute in returnRouteList:
            routeMap[tuple([fRoute[0], rRoute[0]])] = fRoute[1] + rRoute[1]

    # filter out routeMap of keys more than maxTravelDist
    routeMap = [(k, v) for k, v in routeMap.items() if v <= maxTravelDist]

    # sort routeMap based on highest key (aka distance)
    routeMap = sorted(routeMap, key=lambda kv: kv[1])  # [(4000, [1, 2])]

    bestPairs = []
    bestDist = routeMap[-1][0]
    bestPairs.append(routeMap.pop()[1])

    # append any other pairs that are equal to the best pair
    while len(routeMap) > 0:
        nextPair = routeMap.pop()
        if nextPair[0] < bestDist:
            break
        bestPairs.append(nextPair[1])

    return bestPairs


# maxTravelDist = 10000
# forwards = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
# returns = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
# print(optimalUtilization(maxTravelDist, forwards, returns))
