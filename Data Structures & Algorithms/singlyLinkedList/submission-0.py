class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if index == i:
                return curr.value
            i += 1
            curr = curr.next
        return -1
            
    def insertHead(self, val: int) -> None:
        newHead = ListNode(val)
        newHead.next = self.head
        self.head = newHead

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        i = 0
        while curr:
            if not curr.next:
                return False
            if i + 1 == index:
                curr.next = curr.next.next
                return True
            
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values
        
