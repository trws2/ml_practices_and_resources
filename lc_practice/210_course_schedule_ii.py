# runtime: O(numCourses + |prerequisites|)
# space: O(numCourses + |prerequisites|)

# newer implementation
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # compute in-degree for all courses
        in_degree = [0] * numCourses
        for preq in prerequisites:
            in_degree[preq[0]] += 1

        # for adj_list of the course graph
        adj_list = defaultdict(list)
        for preq in prerequisites:
            adj_list[preq[1]].append(preq[0])

        # construct a priority queue with in-degree 0
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        # pop an element from the queue and update in-degree of its children. keep doing this
        # until the queue is empty. return the list of elements in pop order as result
        ret = []
        while len(queue) > 0:
            course = queue.popleft()
            ret.append(course)
            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        if len(ret) != numCourses:
            return []

        return ret


# older implementation
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Step 2: Calculate the in-degree of each node
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            in_degree[course] += 1
        
        # Step 3: Perform topological sort
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check for cycle
        if len(result) < numCourses:
            return []
        
        return result        
