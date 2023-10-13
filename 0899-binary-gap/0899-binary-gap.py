class Solution:
    def binaryGap(self, n: int) -> int:
        s = f'{n:b}'
        result = 0
        for i in range(len(s)):
            if s[i] == '0':
                continue
            for j in range(i + 1, len(s)):
                if s[j] == '0':
                    continue
                result = max(result, j - i)
                break
        return result