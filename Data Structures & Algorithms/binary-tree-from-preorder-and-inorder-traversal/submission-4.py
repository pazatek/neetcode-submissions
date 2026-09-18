# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderValueToInorderIndex = {}
        for index, value in enumerate(inorder):
            preorderValueToInorderIndex[value] = index
        
        preorderRootIndex = 0
        def helper(low, high):
            nonlocal preorderRootIndex
            if low > high:
                return None
            rootValue = preorder[preorderRootIndex]
            preorderRootIndex += 1
            node = TreeNode(rootValue)
            i = preorderValueToInorderIndex[rootValue]
            node.left = helper(low, i - 1)
            node.right = helper(i + 1, high)
            return node
        return helper(0, len(inorder) - 1)







        