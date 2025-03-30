# runtime: serialize O(n), deserialize O(n)
# space: serialize O(n), deserialize O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        ret = []

        def pre_order(node):
            if not node:
                ret.append('N')
                return
            ret.append(str(node.val))
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        index = -1
        data = data.split(',')
        def construct():
            nonlocal index
            index += 1
            v = data[index]
            if v == 'N':
                return None
            node = TreeNode(int(v))
            node.left = construct()
            node.right = construct()
            return node  

        return construct()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
