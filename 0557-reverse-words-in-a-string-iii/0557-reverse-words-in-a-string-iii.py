class Solution:
    def reverseWords(self, s: str) -> str:
        d=s.split()
        t=""
        for i in d:
            t+=i[::-1]
            t+=" "
        return t[:-1]