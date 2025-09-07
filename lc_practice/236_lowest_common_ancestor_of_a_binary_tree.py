# runtime: O(n)
# space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # an important assumption of this problem is both p and q exist in the tree

        # the basic idea is to search for LCA from the tree rooted at root
        # if found, return LCA
        # if not found, return p if found or return q if found
        # if not found either, return null

        if not root:
            return None

        if root.val == p.val:
            return root # found p, return p
        if root.val == q.val:
            return root # found q, return q

        left_return = self.lowestCommonAncestor(root.left, p, q)
        right_return = self.lowestCommonAncestor(root.right, p, q)

        if left_return and right_return:
            return root
        if left_return:
            return left_return
        else:
            return right_return

