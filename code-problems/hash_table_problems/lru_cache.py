"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

"""
Solution
https://docs.python.org/3/library/collections.html#collections.OrderedDict
"""


# First try 1092 ms	22.8 MB


class LRUCache:

    def __init__(self, capacity: int):

        self.recents = collections.deque(maxlen=capacity)
        self.cache = collections.defaultdict(int)

    def cache_update(self, key):
        try:
            self.recents.remove(key)
        except:
            pass
        # since the queue is set to "capacity", this appendleft automatically removes older keys
        # as more recent keys are added
        self.recents.appendleft(key)
        if key not in self.recents:
            del self.cache[key]

    def get(self, key: int):
        # check if recents holds the key
        if not key in self.recents:
            return -1
        self.cache_update(key)
        return self.cache.get(key, -1)  # return -1 if key is not found

    def put(self, key: int, value: int):
        self.cache_update(key)
        self.cache[key] = value


"""
recents = [1]
cache = {1: 1}

recents = [2, 1]
cache = {1: 1, 2: 2}

recents = [1, 2]
cache = {1: 1, 2: 2}

recents = [3, 1]
cache = {1: 1, 2: 2, 3: 3}

cache.get(2);       // returns -1 (not found)


during get and put calls, create a marker stating that the operation is recent
for get, check if the marker is present for given key and return it...
otherwise, key is invalidated
to store the markers, use a queue
if a key is already in this que, then remove it and put the key as the most recent
... to make sure we don't have duplicated keys in this que
?how to check the least recent marker

Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
""""
