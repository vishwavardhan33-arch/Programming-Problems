class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxjump = 0
        end = 0
        ans = 0
        for i in range(len(nums)-1):
            maxjump = max(maxjump,nums[i]+i)
            if maxjump>=len(nums)-1:
                ans+=1
                return ans
            elif end==i:
                ans+=1
                end = maxjump
        return ans