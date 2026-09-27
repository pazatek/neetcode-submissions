class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1 # (grab the rightmost bit of n)
            res = (res << 1) | bit # (make room on the right of res, drop the bit in)
            n >>= 1 # (discard the bit you just read)
        return res