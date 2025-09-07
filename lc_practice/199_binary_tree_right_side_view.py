# runtime: O(n), where n is the number of tree nodes.
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # perform BFS and concatenate the right most element of each level
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))
        ret = []
        prev_level = -1
        prev_val = None
        while queue:
            node, level = queue.popleft()
            if level != prev_level:
                if prev_val is not None:
                    ret.append(prev_val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))                
            prev_level = level
            prev_val = node.val

        if not ret:
            ret.append(prev_val)
        elif prev_val != ret[-1]:
            ret.append(prev_val)

        return ret

