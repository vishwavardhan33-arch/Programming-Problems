class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        # find first element which is greater than its successor for last
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            nums.reverse()
            return
        j = len(nums)-1
        # find the first element which is less than the grater num's predessesor
        while j>=i and nums[j]<=nums[i-1]:
            j-=1
        nums[i-1],nums[j] = nums[j],nums[i-1]
        nums[i:] = reversed(nums[i:])
