class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjL = {}
        for i in range(len(points)):
            adjL[i] = []
        for startNode, coordsi in enumerate(points):
            for endNode, coordsj in enumerate(points):
                if startNode == endNode:
                    continue
                manhattan = abs(coordsi[0] - coordsj[0]) + abs(coordsi[1] - coordsj[1])
                adjL[startNode].append([manhattan, endNode])
        visited = set()
        visited.add(0)
        weight = 0
        minHeap = []
        for manhattan, endNode in adjL[0]:
            heapq.heappush(minHeap, (manhattan, 0, endNode))
        while minHeap:
            manhattan, start, end = heapq.heappop(minHeap)
            if end in visited:
                continue
            weight += manhattan
            visited.add(end)
            for manhattan, neighbor in adjL[end]:
                heapq.heappush(minHeap, (manhattan, end, neighbor))
        return weight
