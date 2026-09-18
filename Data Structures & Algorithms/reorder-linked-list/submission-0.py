# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow fast to find midpoint (slow)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse everything after slow
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        backwardCurr = prev
        curr = head
        while backwardCurr:
            temp = curr.next
            curr.next = backwardCurr
            backwardTemp = backwardCurr.next
            backwardCurr.next = temp
            backwardCurr = backwardTemp
            curr = temp


        
        