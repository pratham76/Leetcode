class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cache = [[0] * n for _ in range(n)]

        for i in range(n):
            cache[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    cache[i][j] = 2 + cache[i + 1][j - 1]
                else:
                    cache[i][j] = max(cache[i + 1][j], cache[i][j - 1])

        return cache[0][n - 1]
