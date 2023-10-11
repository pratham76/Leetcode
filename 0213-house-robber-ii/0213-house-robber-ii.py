class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    
    def helper(self,nums):
            a,b=0,0
            for i in range(len(nums)):
                rob=max(nums[i]+a,b)
                a=b
                b=rob
            return b
        