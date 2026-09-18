class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = {}
        for i in range(n):
            neighbors[i] = []
        for node, neighbor in edges:
            neighbors[node].append(neighbor)
            neighbors[neighbor].append(node)

        visited = set()
        def dfs(node, parent):
            
            if node in visited:
                return False
            visited.add(node)
            for neighbor in neighbors[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n

        


       