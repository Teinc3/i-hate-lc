class Node:
    def __init__(self):
        self.preq: set[int] = set()
    

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # First create all courses as nodes and store them in a hashmap
        courses: dict[int, Node] = {
            x: Node()
            for x in range(numCourses)
        }
        # Then inject all prerequisites
        for preq in prerequisites:
            courses[preq[0]].preq.add(preq[1])
        
        # Now we create "visited" and "visiting" sets
        # Because the problem does not require us to return an order
        # We can optimise with sets
        visited: set[int] = set()
        visiting: set[int] = set()

        # Now, start looping through all nodes
        for uv_course in range(numCourses):
            # If visited already, just skip
            if uv_course in visited:
                continue

            if not self.exploreCourse(
                uv_course, courses, visited, visiting
            ):
                return False
        
        return True
        
    def exploreCourse(
        self, cid: int, courses: dict[int, Node],
        visited: set[int], visiting: set[int]
    ) -> bool:
        # First add the current course to visiting
        visiting.add(cid)

        # Then find all prerequisites
        for preq in courses[cid].preq:
            if preq in visited:
                continue # We already explored it before, try other nodes
            elif preq in visiting:
                return False # Active loop!
            else:
                # unvisited, explore
                result = self.exploreCourse(
                    preq, courses, visited, visiting
                )
                if result == False:
                    return result
        
        # None of the courses fail, so return True and move this node to visited
        visiting.remove(cid)
        visited.add(cid)
        return True
