class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        def f(i,path):
            results.append(path[:])
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                path.append(nums[j])
                f(j+1,path)
                path.pop()
                
        f(0,[])
        return results
            
        
