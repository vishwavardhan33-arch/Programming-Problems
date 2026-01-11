class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        dp1 = [0]*n
        dp2 = [0]*(n+1)
        dp1[1] = nums[0]
        for i in range(1,n-1):
            dp1[i+1] = max(dp1[i],dp1[i-1]+nums[i])
        for j in range(1,n):
            dp2[j+1] = max(dp2[j],dp2[j-1]+nums[j])
        return max(dp1[n-1],dp2[n])

