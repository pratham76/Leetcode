class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        char=set()
        i=0
        for j in range(len(s)):
            if s[j] not in char:
                char.add(s[j])
                length=max(length,j-i+1)
            else:
                while s[j] in char:
                    char.remove(s[i])
                    i+=1
                char.add(s[j])
        return length       


