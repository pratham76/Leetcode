class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return 0
        while n%4==0:
            n=n/4
        return n==1