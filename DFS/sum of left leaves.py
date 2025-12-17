# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def is_leaf(node):
            return node and not node.left and not node.right
        if not root:
            return 0
        sumi = 0
        if root.left and is_leaf(root.left):
            sumi+=root.left.val
        return sumi+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
