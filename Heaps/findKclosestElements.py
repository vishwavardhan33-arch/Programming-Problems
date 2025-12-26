class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        ans = []
        for num in arr:
            heapq.heappush(min_heap,(abs(num-x),num))
        for i in range(k):
            dis,num = heapq.heappop(min_heap)
            ans.append(num)
        ans.sort()
        return ans
