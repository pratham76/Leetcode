class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res=cur=0
        for i in range(len(colors)):
            if i>0 and colors[i]!=colors[i-1]:
                cur=0
            res+=min(cur,neededTime[i])
            cur=max(cur,neededTime[i])
        
        return res