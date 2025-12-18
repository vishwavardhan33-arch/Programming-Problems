class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxjump = 0
        for i in range(len(nums)):
            if maxjump<i: return False
            maxjump = max(maxjump,nums[i]+i)
            if maxjump>=len(nums)-1: return True