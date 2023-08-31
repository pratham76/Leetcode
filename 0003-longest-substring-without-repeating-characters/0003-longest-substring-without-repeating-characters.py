class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        char=set()
        i=0
        for j in range(len(s)):
            if s[j] not in char:
                char.add(s[j])#unique character added
                length=max(length,j-i+1) #update the length after adding the char
            else:
                while s[j] in char:#removes all the old characters(sliding window)
                    char.remove(s[i])
                    i+=1
                char.add(s[j])
        return length