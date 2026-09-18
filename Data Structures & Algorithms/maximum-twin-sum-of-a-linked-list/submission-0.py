# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        forwardStart = slow
        curr = head
        prev = None
        while curr != forwardStart:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = prev
        maxTwinSum = 0
        curTwinSum = 0
        while curr and forwardStart:
            curTwinSum = curr.val + forwardStart.val
            maxTwinSum = max(maxTwinSum, curTwinSum)
            curr = curr.next
            forwardStart = forwardStart.next
        return maxTwinSum