# runtime: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))
        ret = []
        prev_append_level = None
        while queue:
            node, level = queue.popleft()
            if not ret:
                ret.append([node.val])
            else:
                if prev_append_level == level:
                    ret[-1].append(node.val)
                else:
                    ret.append([node.val])

            prev_append_level = level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))                

        return ret

