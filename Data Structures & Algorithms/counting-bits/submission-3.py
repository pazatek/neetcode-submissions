class Solution:
    def countBits(self, n: int) -> List[int]:
        oneCounts = [0]
        for i in range(1, n + 1):
            oneCounts.append(oneCounts[i >> 1] + (i & 1))
        return oneCounts
            