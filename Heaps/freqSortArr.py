class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        minheap = []
        ans = []
        for num,freq in cnt.items():
            heapq.heappush(minheap,(freq,-num))
        while minheap:
            freq,negnum = heapq.heappop(minheap)
            num = -negnum
            ans.extend([num]*freq)
        return ans
