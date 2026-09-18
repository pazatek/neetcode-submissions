class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        pairs = list(freq.items())
        sorted_pairs = sorted(pairs, key=lambda p: p[1], reverse=True)
        vals_and_freqs = sorted_pairs[:k]
        out = []
        for pair in vals_and_freqs:
            out.append(pair[0])
        return out