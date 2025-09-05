class LRUCache:

    def __init__(self, capacity: int):
        self.queue = deque()
        self.capacity = capacity
        self.hashmap = defaultdict(int)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.queue.remove(key)
            self.queue.append(key)
            return self.hashmap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            temp = self.get(key)
        else:
            if len(self.queue) == self.capacity:
                temp = self.queue.popleft()
                del self.hashmap[temp]
            self.queue.append(key)
        self.hashmap[key] = value
        # print(self.queue, self.hashmap)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)