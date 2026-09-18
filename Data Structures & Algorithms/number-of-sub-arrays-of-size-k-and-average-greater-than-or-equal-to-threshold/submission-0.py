class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        runningSum = 0
        out = 0
        for right in range(len(arr)):
            runningSum += arr[right]
            if (right - left) + 1 > k:
                runningSum -= arr[left]
                left += 1
            if ((right - left) + 1 == k) and (k * threshold <= runningSum):
                out += 1
        return out


        