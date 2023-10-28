class Solution:
    def countVowelPermutation(self, n: int) -> int:
            MOD = 10**9 + 7

            # Initialize dynamic programming arrays
            # dp[i][j] represents the number of valid strings of length i ending with vowel j
            dp = [[0] * 5 for _ in range(n + 1)]

            # Base cases: strings of length 1
            for j in range(5):
                dp[1][j] = 1

            # Dynamic programming to count valid strings
            for i in range(2, n + 1):
                dp[i][0] = dp[i - 1][1]  # 'a' can only be followed by 'e'
                dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD  # 'e' can be followed by 'a' or 'i'
                dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD  # 'i' cannot be followed by another 'i'
                dp[i][3] = (dp[i - 1][2] + dp[i - 1][4]) % MOD  # 'o' can be followed by 'i' or 'u'
                dp[i][4] = dp[i - 1][0]  # 'u' can only be followed by 'a'

            # Sum the counts for valid strings of length n
            total_count = sum(dp[n]) % MOD

            return total_count