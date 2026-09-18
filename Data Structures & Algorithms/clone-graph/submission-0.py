"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        originalsToClones = {}
        
        def dfs(originalNode):
             # already been cloned, dont clone again
            if originalNode in originalsToClones:    
                return originalsToClones[originalNode] # gives cloned node
            clone = Node(originalNode.val)
            originalsToClones[originalNode] = clone
            for neighbor in originalNode.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node) if node else None

