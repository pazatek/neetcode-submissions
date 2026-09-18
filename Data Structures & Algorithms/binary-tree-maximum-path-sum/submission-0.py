# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        def bestSum(root):
            if not root:
                return 0
            bestLeft = max(0, bestSum(root.left))
            bestRight = max(0, bestSum(root.right))
            self.maxSum = max(self.maxSum, (bestLeft + bestRight + root.val))
            return max(bestLeft, bestRight) + root.val
        bestSum(root)
        return self.maxSum
