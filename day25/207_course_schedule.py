# runtime: O(|nodes| + |edges|)
# space: O(|nodes| + |edges|)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort solution
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == numCourses

        # # dfs solution
        # pre = defaultdict(list)
        
        # for course, p in prerequisites:
        #     pre[course].append(p)

        # taken = set()

        # def dfs(course):
        #     if not pre[course]:
        #         return True
            
        #     if course in taken:
        #         return False

        #     taken.add(course)

        #     for p in pre[course]:
        #         if not dfs(p):
        #             return False
                
        #     pre[course] = []

        #     return True
        
        # for course in range(numCourses):
        #     if not dfs(course):
        #         return False

        # return True
