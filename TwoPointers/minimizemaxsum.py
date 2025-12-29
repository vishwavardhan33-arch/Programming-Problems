class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        maxi = 0
        while r>l:
            maxi  = max(maxi,nums[r]+nums[l])
            r-=1
            l+=1
        return maxi
