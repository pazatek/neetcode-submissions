class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart = newInterval[0]
        newEnd = newInterval[1]
        newInserted = False
        for start, end in intervals:
            if end < newStart:
                result.append([start,end])
            elif start > newEnd:
                if newInserted == False:
                    result.append([newStart, newEnd])
                    newInserted = True
                result.append([start, end])
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        if newInserted == False:
            result.append([newStart, newEnd])
        return result