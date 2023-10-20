class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        def kadane(i):
            if F[i] != None:
                return F[i]
            F[i] = max(nums[i],kadane(i-1) + nums[i])
            return F[i]
        n = len(nums)
        F = [None for _ in range(n)]
        F[0] = nums[0]
        kadane(n-1)
        return max(F)
        """
        maxsub=nums[0]
        cursum=0
        for i in range(len(nums)):
            if cursum<0:
                cursum=0
            cursum+=nums[i]
            maxsub=max(maxsub,cursum)
            
        return maxsub