# runtime: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # the diameter of a binary tree can be passing through root or not passing 
        # throught root.
        #
        # if passing through root, it will be 2 + the max path passing through right
        # child and the max path passing through left child. Note the max path of
        # left/right child can only be from its left grandchild or the right grandchild,
        # it cannot includ both of grandchildren
        #
        # if not passing through root, it will max path return from either left child
        # or the right child.
        #
        # we need to maintain a non-local variable to keep track of the current max
        # path from its children without passing through root.

        self.ans = 0
        self.max_one_way_path(root)
        return self.ans

    def max_one_way_path(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        left = 1 + self.max_one_way_path(root.left)
        right = 1 + self.max_one_way_path(root.right)        

        self.ans = max(self.ans, left + right)

        return max(left, right)

