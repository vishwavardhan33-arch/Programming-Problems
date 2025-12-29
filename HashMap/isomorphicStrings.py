class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        map_s = {}
        map_t = {}
        for c1,c2 in zip(s,t):
            if c1 in map_s:
                if map_s[c1]!=c2:
                    return False
            else:
                map_s[c1]=c2
            if c2 in map_t:
                if map_t[c2]!=c1:
                    return False
            else:
                map_t[c2]=c1
        return True
        
        
