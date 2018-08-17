# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
# operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4



class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            n = self.dict[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.remove(self.dict[key])
        n = Node(key, value)
        self.add(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dict[n.key]

    def remove(self, n):
        p = n.prev
        q = n.next
        p.next = q
        q.prev = p

    def add(self, n):
        p = self.tail.prev
        p.next = n
        n.prev = p
        self.tail.prev = n
        n.next = self.tail


        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)