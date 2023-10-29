class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        pow_ = a = b = 0

        while n > 0:
            n, m = divmod(n, 10)
            if m < 2 and n > 0:
                m += 10
                n -= 1
            
            a += min(9, m - 1) * 10 ** pow_
            b += max(m - 9, 1) * 10 ** pow_
            pow_ += 1

        return a, b