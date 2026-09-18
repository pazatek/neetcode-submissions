class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        runningMax = -1
        
        for i in range (len(arr) - 1, -1, -1):
                temp = arr[i]
                arr[i] = runningMax
                if temp > runningMax:
                    runningMax = temp

        return arr


