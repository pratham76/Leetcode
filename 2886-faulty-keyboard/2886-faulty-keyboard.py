class Solution:
    def finalString(self, s: str) -> str:
        rev=""
        for i in range(len(s)):
            if s[i]=="i":
                rev=rev[::-1]
            else:
                rev+=s[i]
        return rev

        