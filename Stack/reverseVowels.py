class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        stack =[]
        res = ""
        for i in s:
            if i in vowels:
                stack.append(i)
        for i in s:
            if i in vowels:
                res +=stack.pop()
            else:
                res+=i
        return res
