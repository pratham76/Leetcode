class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        
        t1=len(text1)
        t2=len(text2)
        dp=[[0]*(t2+1) for _ in range(t1+1)]

        for i in range(t1-1,-1,-1):
            for j in range(t2-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
        """

        t1,t2=len(text1),len(text2)
        dp=[[0]*(t2+1) for _ in range(t1+1)]

        for i in range(t1-1,-1,-1):
            for j in range(t2-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
        