class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.kvs = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.kvs:
            old = self.kvs[key]
            old.prev.next = old.next
            old.next.prev = old.prev

            old.next = self.tail
            old.prev = self.tail.prev
            self.tail.prev.next = old
            self.tail.prev = old
            
            return self.kvs[key].val #returns the val of node

        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        # update (key, value), remove it from cache
        if key in self.kvs:
            old = self.kvs[key]
            old.prev.next = old.next
            old.next.prev = old.prev
        
        # put  (key, value) as most recently used
        newnode = ListNode(key,value)

        newnode.prev = self.tail.prev
        newnode.next = self.tail
        self.tail.prev = newnode
        newnode.prev.next = newnode

        self.kvs[key] = newnode

        # if new pair causes cache to exceed capacity, remove lru   
        if len(self.kvs) > self.cap:
            lru = self.head.next
            self.head.next = lru.next
            lru.next.prev = self.head
            del self.kvs[lru.key]

        
