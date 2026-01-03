# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return [True,0]
            leftbalanced, left = height(root.left)
            rightbalanced, right = height(root.right)
            is_balanced = leftbalanced and rightbalanced and abs(left-right)<=1
            return [is_balanced,1+max(left,right)]
        return height(root)[0]
