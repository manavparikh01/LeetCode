class ListNode:

    def __init__(self, key= -1, val= -1, next= None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.arr = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key%len(self.arr)

    def put(self, key: int, value: int) -> None:
        ind = self.hash(key)
        curr = self.arr[ind]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, val = value)

    def get(self, key: int) -> int:
        ind = self.hash(key)
        curr = self.arr[ind].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        ind = self.hash(key)
        curr = self.arr[ind]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)