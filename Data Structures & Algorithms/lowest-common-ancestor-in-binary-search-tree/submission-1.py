# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lesser = min(p.val, q.val)
        greater = max(p.val, q.val)
        ancestor = root
        while root:
            if lesser <= root.val and greater >= root.val:
                ancestor = root
                break
            elif lesser < root.val:
                root = root.left
            elif greater > root.val:
                root = root.right
        return ancestor


