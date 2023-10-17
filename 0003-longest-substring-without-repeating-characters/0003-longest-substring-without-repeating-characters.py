class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=0
        j=0
        char=set()
        for i in range(len(s)):
            if s[i] not in char:
                char.add(s[i])
                length=max(length,i-j+1)
            else:
                while s[i] in char:
                    char.remove(s[j])
                    j+=1
                char.add(s[i])
        return length
        