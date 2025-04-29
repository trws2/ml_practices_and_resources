# runtime: O(numCourses + |prerequisites|)
# space: O(numCourses + |prerequisites|)

# newer implementation
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # compute in-degree for all courses
        in_degree = [0] * numCourses
        for preq in prerequisites:
            in_degree[preq[0]] += 1

        adj_list = defaultdict(list)
        for preq in prerequisites:
            adj_list[preq[1]].append(preq[0])

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        num_courses_popped = 0
        while len(queue) > 0:
            course = queue.popleft()
            print(f"course popped = {course}")
            num_courses_popped += 1
            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        if num_courses_popped == numCourses:
            return True

        return False


# older implementation
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialization: adjancency list, indegree list, final answer
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        # initialize priority queue with node (course) with indegree 0        queue = deque()
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # keep poping node (course) from the queue as course taken
        # for each course that can be taken next, decrement its indegree
        # when indegree reach 0, append it to the priority queue.
        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == numCourses
