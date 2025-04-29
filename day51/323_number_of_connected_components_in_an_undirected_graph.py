# runtime: O(|V| + |E|)
# space: 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in adj_list[node]:
                dfs(nei)
            

        visited = set()
        count = 0
        for node in range(n):
            if node in visited:
                continue
            dfs(node)
            count += 1
        
        return count
