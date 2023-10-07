import heapq

# Min Heap
heap = []
for x in range(10):
    heapq.heappush(heap, x)
    print(heap)

# Max Heap
heap = []
for x in range(10, -1, -1):
    heapq.heappush(heap, x)
    print(heap)

# pops off the nodes that are NOT in order
# while len(heap):
    # print(heap.pop())

# pop offs the lowest numbers first
while heap:
    print(heapq.heappop(heap))

# So if we wanted to only keep track of only two highest numbers...
LIMIT = 6
heap = []
for x in range(10, -1, -1):
    if len(heap) < LIMIT:
        heapq.heappush(heap, x)
    else:

        print(heap, "last element = ", heap.pop())
while heap:
    # Prints numbers as they appear in the binary tree 9, 8, 10, 6, 7, 5
    # print(heap.pop())

    # Prints numbers from lowest to highest 5, 6, 7, 8, 9, 10
    print(heapq.heappop(heap))

# Print the 4th largest number
print(heapq.nlargest(4, range(10))[-1])
