class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseToPrereqs = {}
        for i in range(numCourses):
            courseToPrereqs[i] = []
        for course, prereq in prerequisites:
            courseToPrereqs[course].append(prereq)

        visited = set()
        done = set()
        path = []
        def dfs(course):
            if course in visited:
                return False
            if course in done:
                return True
            visited.add(course)
            for prereq in courseToPrereqs[course]:
                if not dfs(prereq):
                    return False
            path.append(course)
            visited.remove(course)
            done.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return path
            

        