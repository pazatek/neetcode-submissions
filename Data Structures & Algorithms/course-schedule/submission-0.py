class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {}
        for i in range(numCourses):
            prereqMap[i] = []
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        visitedSet = set()

        def dfs(course):
            if course in visitedSet:
                return False       
            if prereqMap[course] == []:
                return True

            visitedSet.add(course)

            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            visitedSet.remove(course)
            prereqMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True