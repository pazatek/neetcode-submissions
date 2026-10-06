class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjL = {}
        for i in range(1, n + 1):
            adjL[i] = []
        for start, end, time in times:
            adjL[start].append([time,end])
        visited = set()

        minHeap = []
        heapq.heappush(minHeap, [0, k])
        while minHeap:
            time, dest = heapq.heappop(minHeap)
            if dest in visited:
                continue
            visited.add(dest)
            signalLength = time
            for weight, neighbor in adjL[dest]:
                heapq.heappush(minHeap, [time + weight, neighbor])
        return signalLength if len(visited) == n else -1
