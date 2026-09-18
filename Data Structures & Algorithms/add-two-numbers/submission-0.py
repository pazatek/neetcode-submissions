# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            sumOfNodes = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = 0   # reset carry, now that it is in sum

            if sumOfNodes > 9:
                sumOfNodes -= 10
                carry += 1

            # move sum list forward
            curr.next = ListNode(sumOfNodes)
            curr = curr.next

            # move input list(s) forward
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next