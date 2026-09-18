class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0    

    def get(self, index: int) -> int:
        curr = self.head
        if index < 0 or index >= self.size:
            return -1
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        if self.size == 0:
            self.addAtHead(val)
            return
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head
    
        for i in range(index):
            prev = curr
            curr = curr.next 
        prev.next = Node(val, curr)

        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for i in range(index):
                prev = curr
                curr = curr.next 
            prev.next = curr.next
        self.size -= 1
        return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)