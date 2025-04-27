# runtime: O(n + |queries|)
# space: O(n + |queries|)

# the passing solution is very simple, no need for DFS and connected component search
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        if n == 0:
            return []

        # self parent
        groupStart = [i for i in range(n)]
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                groupStart[i] = groupStart[i - 1]

        result = []
        for u, v in queries:
            if u == v:
                result.append(True)
            else:
                result.append(groupStart[u] == groupStart[v])

        return result


# the following solution run out of memory
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # construct adj list
        adj_list = defaultdict(list)
        for i in range(n):
            adj_list[i] = []
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if abs(num - nums[j]) <= maxDiff:
                    adj_list[j].append(i)
                    adj_list[i].append(j)                    

        # construct connected component sets
        node_to_visit_map = {}
        def dfs(node, visited):
            visited.add(node)
            node_to_visit_map[node] = visited
            neis = adj_list[node]
            for nei in neis:
                if nei not in visited:
                    dfs(nei, visited)
                
        
        for node in range(n):
            if node in node_to_visit_map:
                continue            
            visited = set()
            dfs(node, visited)
        
        ret = []
        for q in queries:
            if node_to_visit_map[q[0]] is node_to_visit_map[q[1]]:
                ret.append(True)
            else:
                ret.append(False)
        
        return ret


# the following solution takes too long to run
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # construct adj list
        adj_list = defaultdict(list)
        for i in range(n):
            adj_list[i] = []
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if abs(num - nums[j]) <= maxDiff:
                    adj_list[j].append(i)
                    adj_list[i].append(j)                    

        query_set = defaultdict(list)
        starting_nodes = set()
        ret = []
        for i, q in enumerate(queries):
            if q[0] == q[1]:
                ret.append(True)
                continue
            
            query_set[(q[0], q[1])].append(i)
            starting_nodes.add(q[0])
            ret.append(False)

        # dfs for each starting node in the query and construct which node it can be reached.
        # we can do early stop if all the target node has been reach. 
        def dfs(node):
            if visit_status[node] != 0:
                return
            visit_status[node] = 1
            neis = adj_list[node]
            for nei in neis:
                indices = query_set.get((start_node, nei), [])
                
                if indices:
                    for ind in indices:
                        ret[ind] = True
                    del query_set[(start_node, nei)]
                    if len(query_set) == 0:
                        return ret
                dfs(nei)
            visit_status[node] = 2
                
        for start_node in starting_nodes:
            visit_status = [0 for _ in range(n)] # 0 not yet visit; 1 being visit; 2 visited                 
            dfs(start_node)
        
        return ret
    


