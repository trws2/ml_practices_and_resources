# runtime: O(n)
# space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}

        def cloneGraphAux(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            
            if node.val in node_map:
                return node_map[node.val]

            new_node = Node(node.val, [])
            node_map[node.val] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(cloneGraphAux(nei))
            return new_node

        return cloneGraphAux(node)
