"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # head = [val, random_index]
        copy = {}
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        for node in copy:
            if node.next:
                copy[node].next = copy[node.next]
            if node.random:
                copy[node].random = copy[node.random]
        return copy[head] if head else None