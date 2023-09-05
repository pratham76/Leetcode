class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count=[0]*(n+1)
        trusted_count=[0]*(n+1)
        if n == 1:
            return 1
        for t in trust:
            a,b=t
            trust_count[a]+=1
            trusted_count[b]+=1
        for i in range(n+1):
            if trust_count[i]==0 and trusted_count[i]==n-1:
                return i
        return -1


        