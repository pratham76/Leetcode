class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        hash=Counter(nums)
        minc=len(nums)/3
        for i in hash:
            if hash[i]>minc:
                res.append(i)
        return res
