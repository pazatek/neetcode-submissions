# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        out = []
        if root:
            q.append(root)
        while len(q) > 0:
            levelLength = len(q)
            for i in range(levelLength):
                curr = q.popleft()
                if i == levelLength - 1:
                    out.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return out