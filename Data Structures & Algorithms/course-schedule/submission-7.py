class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}

        for i in range(numCourses):
            prereqs[i] = []
        
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        seen = set()
        def dfs(course):
            if course in seen:
                return False
            seen.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            prereqs[course] = []
            return True
        
        for course in prereqs:
            if not dfs(course):
                return False
        return True
        