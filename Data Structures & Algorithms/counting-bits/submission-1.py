class Solution:
    def countBits(self, n: int) -> List[int]:
        oneCounts = []
        count = 0
        for i in range(n + 1):
            temp = i
            while temp:
                count += temp & 1
                temp >>= 1
            oneCounts.append(count)
            count = 0
        return oneCounts
            