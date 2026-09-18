class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-weight for weight in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            heaviest = -heapq.heappop(heap)
            secondheaviest = -heapq.heappop(heap)
            if heaviest == secondheaviest:
                continue
            else:
                heapq.heappush(heap, -(heaviest-secondheaviest))
        return -heap[0] if heap else 0
        