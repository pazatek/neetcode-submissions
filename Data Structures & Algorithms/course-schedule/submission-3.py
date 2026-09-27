class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereqs = {}

        for i in range(numCourses):
            courseToPrereqs[i] = []

        for course, prereq in prerequisites:
            courseToPrereqs[course].append(prereq)
        
        def dfs(course):
            if courseToPrereqs[course] == []:
                return True

            if course in seen:
                return False
            seen.add(course)
            for prereq in courseToPrereqs[course]:
                if not dfs(prereq):
                    return False
            seen.remove(course)
            courseToPrereqs[course] = []
            return True
        seen = set()
        for course in courseToPrereqs:
            if not dfs(course):
                return False
        return True
        