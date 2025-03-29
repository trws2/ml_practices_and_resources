# runtime: get O(1), put O(1)
# space: get O(capacity), put O(capacity)

class LinkedListNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedListNode() # dummy node
        self.tail = LinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def get(self, key: int) -> int:
        node = self.map.get(key, None)
        if not node:
            return -1
        # update list to make the node most recently used.
        node.next.prev = node.prev
        node.prev.next = node.next

        n = self.head.next
        node.next = n
        node.prev = self.head        
        n.prev = node
        self.head.next = node        

        return node.value

    def put(self, key: int, value: int) -> None:
        # if cache in capacity, remove the least recently used one and then add the node
        # if not, add the node.
        # node should be add/update to the front of the list
        if key in self.map:
            node = self.map[key]
            node.value = value            
            node.next.prev = node.prev
            node.prev.next = node.next
        else:
            node = LinkedListNode()
            node.key = key
            node.value = value
            if len(self.map) == self.capacity:
                # remove the least recently used one.
                del self.map[self.tail.prev.key]
                n = self.tail.prev.prev
                n.next = self.tail
                self.tail.prev = n

        n = self.head.next
        node.next = n
        node.prev = self.head        
        n.prev = node
        self.head.next = node

        self.map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
