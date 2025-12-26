class Solution:
    def frequencySort(self, s: str) -> str:
        cnt  = Counter(s)
        max_heap = []
        ans = []
        for ch,freq in cnt.items():
            heapq.heappush(max_heap,(-freq,ch))
        while max_heap:
            neg_freq,ch = heapq.heappop(max_heap)
            ans.append(ch*-neg_freq)

        return "".join(ans)
