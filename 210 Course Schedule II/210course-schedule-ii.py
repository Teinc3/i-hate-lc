class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs: dict[int, set[int]] = {
            x: set() for x in range(numCourses)
        }

        for preq in prerequisites:
            preqs[preq[0]].add(preq[1])

        visited: set[int] = set()
        visiting: set[int] = set()
        stack: list[int] = []
        # Explore all unexplored nodes
        for course in range(numCourses):
            visiting.clear()
            if not self.exploreCourse(course, preqs, visited, visiting, stack):
                return []
        
        return stack
            
    def exploreCourse(
        self, course: int, preqs: dict[int, set[int]],
        visited: set[int], visiting: set[int], stack: list[int]
    ) -> bool:
        if course in visited:
            return True
        elif course in visiting:
            return False

        # Currently visiting this course
        visiting.add(course)
        
        # DFS all prerequisites.
        for preq in preqs[course]:
            if not self.exploreCourse(preq, preqs, visited, visiting, stack):
                # Error, return
                return False
            
        # All good, add this node to the end and remove from visiting
        visited.add(course)
        stack.append(course)
        visiting.remove(course)
        return True
