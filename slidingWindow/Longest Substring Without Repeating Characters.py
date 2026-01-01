class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        letters = set()
        curr = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in letters:
                letters.remove(s[start])
                start+=1
                curr-=1
            curr+=1
            ans = max(ans,curr)
            letters.add(s[i])
        return ans
