class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for i in s:
            if i.isalnum():
                r+=i
        r=r.lower()
        print(r)
        if r==r[::-1]:
            return True
        