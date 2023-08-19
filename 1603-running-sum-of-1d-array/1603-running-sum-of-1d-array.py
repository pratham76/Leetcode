class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum=[0]*len(nums)
        rsum[0]=nums[0]
        for i in range(1,len(nums)):
            rsum[i]=rsum[i-1]+nums[i]
        
        return rsum
