class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = {}
        for i in range(1, n + 1):
            adjacencyList[i] = []
        for source, target, time in times:
            adjacencyList[source].append((time, target))
        
        shortest = {}
        minHeap = [(0, k)]
        while minHeap:
            time1, node1 = heapq.heappop(minHeap)
            if node1 not in shortest:
                shortest[node1] = time1
                for neighborTime, neighbor in adjacencyList[node1]:
                    if neighbor not in shortest:
                        heapq.heappush(minHeap, (time1 + neighborTime, neighbor))
        return max(shortest.values()) if len(shortest) == n else -1

