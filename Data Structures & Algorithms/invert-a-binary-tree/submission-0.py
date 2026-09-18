# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        if root:
            q.append(root)
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                temp = curr.right
                curr.right = curr.left
                curr.left = temp
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root
        