class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        total = 0
        maxi = float('-inf')
        for j in range(len(nums)):
            total+=nums[j]
            while (j-i+1)==k:
                maxi = max(maxi,total/k)
                total-=nums[i]
                i+=1
        return maxi
