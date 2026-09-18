# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while (len(lists) > 1):
            out = []
            for i in range(0, len(lists), 2):

                list1 = lists[i]

                if (i == len(lists) - 1):
                    list2 = None
                else:
                    list2 = lists[i+1]

                dummy = ListNode()
                tail = dummy
                while list1 and list2:
                    if list1.val < list2.val:
                        tail.next = list1
                        list1 = list1.next
                        tail = tail.next
                    else:
                        tail.next = list2
                        list2 = list2.next
                        tail = tail.next
                tail.next = list1 or list2
                out.append(dummy.next)
            lists = out
        return lists[0] if lists else None

                