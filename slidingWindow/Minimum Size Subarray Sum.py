class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        start = 0
        mini = float('inf')
        for i in range(len(nums)):
            curr+=nums[i]
            while curr>=target:
                if i-start+1<mini:
                    mini = i-start+1
                curr-=nums[start]
                start+=1
                
        return mini if mini!= float('inf') else 0


