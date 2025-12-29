class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map = {}
        for word in strs:
            sort = "".join(sorted(word))
            if sort in map:
                map[sort].append(word)
            else:
                map[sort]  = [word]
        for list in map.values():
            res.append(list)
        return res
