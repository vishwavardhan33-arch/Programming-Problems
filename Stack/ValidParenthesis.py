class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_list = []
        oc_dict = {'{': '}', '[': ']', '(': ')'}

        for i in s:
            if i in '{[(':
                open_list.append(i)
            else:
                if len(open_list) != 0 and oc_dict[open_list[-1]] == i:
                    open_list.pop()
                else:
                    return False
        
        if len(open_list) == 0:
            return True
        else:
            return False
