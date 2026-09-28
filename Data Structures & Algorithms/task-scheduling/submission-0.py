class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        charCounts = {}
        for char in tasks:
            if char in charCounts:
                charCounts[char] += 1
            else:
                charCounts[char] = 1
        q = deque()
        heap = []
        for char in charCounts:
            heapq.heappush(heap, -charCounts[char])
        time = 0
        while heap or q:
            time += 1
            if heap:
                charsLeft = heapq.heappop(heap) + 1
                if charsLeft != 0:
                    q.append((time+n, charsLeft)) # waitTill, -charCounts[char]
            if q and q[0][0] == time:
                ready = q.popleft()
                heapq.heappush(heap, ready[1])
        return time
            