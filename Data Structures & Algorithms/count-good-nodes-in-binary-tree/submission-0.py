# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxAncestor = root.val
        count = 0
        def recurse(root, maxAncestor):
            count = 0
            if not root:
                return 0
            if root.val >= maxAncestor:
                count = 1
            maxAncestor = max(maxAncestor, root.val)
            
            return count + recurse(root.right, maxAncestor) + recurse(root.left, maxAncestor)

        return recurse(root, maxAncestor)

        