class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash=set()
        length=0
        j=0
        for i in range(len(s)):
            if s[i] not in hash:
                hash.add(s[i]) 
                length=max(length,i-j+1)
            else:
                while s[i] in hash:
                    hash.remove(s[j])
                    j+=1
                hash.add(s[i])
        return length       


