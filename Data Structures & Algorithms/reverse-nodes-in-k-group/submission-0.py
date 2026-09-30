# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        beforeGroup = dummy
        # while we have a group to be before
        while beforeGroup:
            groupEnd = self.getKthNode(beforeGroup, k)
            if not groupEnd:
                break
            nextGroupStart = groupEnd.next
            curr = beforeGroup.next
            prev = nextGroupStart
            # reverse this group
            while curr != nextGroupStart:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = beforeGroup.next
            beforeGroup.next = groupEnd
            beforeGroup = temp
        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

           

        