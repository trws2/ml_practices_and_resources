# runtime: O(n)
# space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth(root) >= 0

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth_left = self.depth(root.left)
        depth_right =  self.depth(root.right)

        if depth_left < 0 or depth_right < 0:
            return -1

        if abs(depth_left - depth_right) > 1:
            return -1

        return max(depth_left, depth_right) + 1
        
