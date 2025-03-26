# runtime: O(n^2)
# space: O(n^2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        preorder = deque(preorder)

        def build(preorder, inorder):
            if not inorder:
                return None

            val = preorder.popleft()
            idx = inorder.index(val)
            root = TreeNode(val)

            root.left = build(preorder, inorder[:idx])
            root.right = build(preorder, inorder[idx+1:])            

            return root

        return build(preorder, inorder)
        

