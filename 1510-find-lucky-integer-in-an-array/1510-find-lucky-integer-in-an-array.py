class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash=Counter(arr)
        res=-1
        for ele,val in hash.items():
            if ele==val:
                res=max(res,ele)
        return res

        