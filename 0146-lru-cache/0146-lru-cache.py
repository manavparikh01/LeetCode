class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nextn = node.next
        prev.next = nextn
        nextn.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nextn = self.right
        prev.next = node
        nextn.prev = node
        node.prev = prev
        node.next = nextn

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.hashmap[key].val = value
        else:
            self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])
        if len(self.hashmap) > self.cap:
            left_node = self.left.next
            self.remove(left_node)
            del self.hashmap[left_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)