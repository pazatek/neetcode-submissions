class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        runningMax = -1
        
        for i in range (len(arr) - 1, -1, -1):

            if arr[i] < runningMax:
                arr[i] = runningMax

            else:
                temp = arr[i]
                arr[i] = runningMax
                runningMax = temp
                
        return arr


