class Solution:
    def toLowerCase(self, s: str) -> str:
        res=""
        for i in s:
            res+=i.lower()
        return res
        