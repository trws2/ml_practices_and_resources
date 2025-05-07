# runtime: O(n), where n is number of tree nodes
# space: O(1)

# newer implementation which I think is more correct.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findNode(node: 'TreeNode', p: 'TreeNode'):
            if node is None:
                return None

            if node.val == p.val:
                return node
            
            ret_left = findNode(node.left, p)
            if ret_left:
                return ret_left

            ret_right = findNode(node.right, p)
            if ret_right:
                return ret_right

            return None

        def findLCA(node: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            if node is None:
                return (None, False)
            
            if node.left is None and node.right is None:
                if node.val == p.val:
                    return (p, False)
                if node.val == q.val:
                    return (q, False)
                return (None, False)

            if node.val == p.val:
                ret_left = findNode(node.left, q)
                ret_right = findNode(node.right, q)                    
                if ret_left is not None:
                    return (node, True)
                if ret_right is not None:
                    return (node, True)
                return (node, False)
            elif node.val == q.val:
                ret_left = findNode(node.left, p)
                ret_right = findNode(node.right, p)                    
                if ret_left is not None:
                    return (node, True)
                if ret_right is not None:
                    return (node, True)
                return (node, False)
            else:
                ret_left = findLCA(node.left, p, q)
                ret_right = findLCA(node.right, p, q)                
                
                if ret_left[1]:
                    return ret_left
                if ret_right[1]:
                    return ret_right
                if ret_right[0] is not None and ret_left[0] is not None:
                    return (node, True)
                if ret_right[0] is not None:
                    return ret_right
                if ret_left[0] is not None:
                    return ret_left
                return (None, False)
        
        res = findLCA(root, p, q)
        return res[0]


# older implementation that pass all test cases

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val:
            return p
        if root.val == q.val:
            return q

        left_return = self.lowestCommonAncestor(root.left, p, q)
        right_return = self.lowestCommonAncestor(root.right, p, q)        

        if left_return and right_return:
            return root
        if left_return:
            return left_return
        
        return right_return


