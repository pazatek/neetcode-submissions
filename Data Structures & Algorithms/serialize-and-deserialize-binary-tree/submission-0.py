# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        chars = []
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                out = q.popleft()
                if not out:
                    chars.append('N')
                    continue
                chars.append(str(out.val))
                q.append(out.left)
                q.append(out.right)
        return ",".join(chars)
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        if tokens[0] == 'N':
            return None
        root = TreeNode(int(tokens[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if tokens[i] != 'N':
                node.left = TreeNode(int(tokens[i]))
                q.append(node.left)
            if tokens[i + 1] != 'N':
                node.right = TreeNode(int(tokens[i+1]))
                q.append(node.right)
            i += 2
        return root

