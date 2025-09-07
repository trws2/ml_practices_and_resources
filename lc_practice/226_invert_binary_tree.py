# runtime: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap left and right child of current root
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursively swap left and right child
        self.invertTree(root.left)
        self.invertTree(root.right)        

        return root
