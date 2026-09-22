class TimeMap:

    def __init__(self):
        self.timeMap = {}
         
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = [(timestamp,value)]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        left = 0
        right = len(self.timeMap[key]) - 1
        closest = ""
        while left <= right:
            mid = (left + right) // 2
            if self.timeMap[key][mid][0] > timestamp:
                right = mid - 1
            elif self.timeMap[key][mid][0] <= timestamp:
                closest = self.timeMap[key][mid][1]
                left = mid + 1
        return closest

        
