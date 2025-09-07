# runtime: O(K)
# space: O(K)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: Optional[TreeNode], ret: List[int]):
            if not root:
                return
            if len(ret) == k:
                return
            inorder(root.left, ret)
            if len(ret) == k:
                return            
            ret.append(root.val)
            if len(ret) == k:
                return
            inorder(root.right, ret)
            return

        if not root:
            return -1

        ret = []
        inorder(root, ret)
        return ret[-1]
        
