"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        count = 0
        endIndex = 0
        for index in range(len(starts)):
            if starts[index] < ends[endIndex]:
                count += 1
            else:
                endIndex += 1
        return count
        