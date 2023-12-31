"""

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

import heapq
import collections

points = [[3, 3], [5, -1], [-2, 4]]
K = 2


def closest(point, K):
    """Time: n + nlogk where k is the size of the heap"""
    points_dist = [(point[0]**2 + point[1]**2, point) for point in points]
    return [point[1] for point in heapq.nsmallest(K, points_dist)]


print(closest(points, K))


def closest_two(points, K):
    heap = []
    for point in points:
        dist = -(point[0]**2 + point[1]**2)
        if len(heap) == K:
            heapq.heappushpop(heap, (dist, point))
        else:
            heapq.heappush(heap, (dist, point))
    return [point[1] for point in heap]


print(closest_two(points, K))
