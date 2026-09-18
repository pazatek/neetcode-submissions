from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slowest = 1
        fastest = max(piles)
        while slowest <= fastest:
            k = (slowest+fastest)//2
            hoursTaken = 0
            for bananas in piles:
                hoursTaken += ceil(bananas/k)
            if hoursTaken <= h:
                slowestPass = k
                fastest = k - 1
            else:
                slowest = k + 1
        return slowestPass