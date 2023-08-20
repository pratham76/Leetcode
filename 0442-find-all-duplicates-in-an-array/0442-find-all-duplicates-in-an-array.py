class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h=Counter(nums)
        res=[]
        for i in h:
            if h[i]>1:
                res.append(i)
        return res
                