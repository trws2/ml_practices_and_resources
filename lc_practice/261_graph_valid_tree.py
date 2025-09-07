class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for edge in edges:
            s = edge[0]
            e = edge[1]

            adj_list[s].append(e)
            adj_list[e].append(s)
        
        def detect_cycle(node, parent):
            # done visiting
            if visited[node] == 2:
                return False
            
            # being visit; cycle detected
            if visited[node] == 1:
                return True

            visited[node] = 1
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if detect_cycle(nei, node):
                    return True
                
            # done visiting
            visited[node] = 2

        connected_component_count = 0
        visited = [0 for _ in range(n)]
        for i in range(n):
            if visited[i] != 0:
                continue
            if detect_cycle(i, -1):
                return False
            connected_component_count += 1
            if connected_component_count > 1:
                return False
        
        return True

