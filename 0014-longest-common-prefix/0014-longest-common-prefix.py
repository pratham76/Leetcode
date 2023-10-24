class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        minlen=min(len(i) for i in strs)
        
        for i in range(minlen):
            char=strs[0][i]
            
            for s in strs[1:]:
                if char!=s[i]:
                    return strs[0][:i]
        return strs[0][:minlen]
                    