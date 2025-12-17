# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        maxi = float('-inf')
        q = deque([root])
        num = 1
        maxnum = 1
        while q:
            level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                level_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_sum>maxi:
                maxi = level_sum
                maxnum = num
            num+=1
        return maxnum