class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        m = 0
        hi = len(nums)-1
        while(m<=hi):
            if nums[m]==0:
                nums[lo],nums[m] = nums[m],nums[lo]
                m+=1
                lo+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[hi] = nums[hi],nums[m]
                hi-=1
        

