class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=""
        t1=""
        for i in range(len(s)):
            if s[i]!="#":
                s1+=s[i]
            else:
                s1=s1[:-1]
        
        for i in range(len(t)):
            if t[i]!="#":
                t1+=t[i]
            else:
                t1=t1[:-1]
        if s1==t1:
            return True
        return False
        
