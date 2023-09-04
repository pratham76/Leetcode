class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for sub_len in range(1,len(s)//2+1):
            if len(s)%sub_len==0:
                substr=s[:sub_len]
                if substr*(len(s)//sub_len)==s:
                    return True
        return False

        