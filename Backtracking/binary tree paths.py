# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res = []
        def f(node,path,res):
            if not node :
                return 
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(path[:]))
            else:
                f(node.left,path,res)
                f(node.right,path,res)
            path.pop()
        f(root,[],res)
        return res 
