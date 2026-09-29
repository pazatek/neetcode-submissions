class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjL = {}
        for i in range(n):
            adjL[i] = []
        for start, end, weight in edges:
            adjL[start].append([weight, end])

        visited = set()
        heap = []
        heapq.heappush(heap, ([0, src]))
        result = {}
        while heap:
            distance, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            result[node] = distance
            for weight, neighbor in adjL[node]:
                heapq.heappush(heap,[weight + distance, neighbor])
        for i in range(n):
            if i not in result:
                result[i] = -1
        return result


        
