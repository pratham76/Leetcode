class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        currmin,currmax=1,1
        for i in range(len(nums)):
            if nums[i]==0:
                currmin,currmax=1,1
                continue
            temp=currmax*nums[i]
            currmax=max(currmax*nums[i],nums[i],nums[i]*currmin)
            currmin=min(temp,nums[i],nums[i]*currmin)
            res=max(currmax,currmin,res)
        
        return res

            
        