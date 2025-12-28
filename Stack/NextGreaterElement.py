class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None
        map = {}
        res = []
        stack = []
        stack.append(nums2[0])
        for i in range(1,len(nums2)):
            while stack and nums2[i]>stack[-1]:
                map[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        for num in stack:
            map[num] = -1
        for num in nums1:
            res.append(map[num])
        return res
