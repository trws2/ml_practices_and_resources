# runtime: O(n)
# space: O(tree_depth)

# newer implementation

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def depth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_depth = depth(node.left)
            if left_depth < 0:
                return -1

            right_depth = depth(node.right)
            if right_depth < 0:
                return -1

            if abs(left_depth - right_depth) > 1:
                return -1

            return 1 + max(left_depth, right_depth)

        left_depth = depth(root.left)
        if left_depth < 0:
            return False

        right_depth = depth(root.right)
        if right_depth < 0:
            return False

        if abs(left_depth - right_depth) > 1:
            return False

        return True


# older implementation

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



