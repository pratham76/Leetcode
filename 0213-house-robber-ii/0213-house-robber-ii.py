class Solution(object):
    def rob(self, nums):
        if not nums:
            return
        return max(nums[0], self.helper(nums[1:]),self.helper(nums[:-1]))
        
    def helper(self,nums):
        rob1,rob2=0,0

        for n in nums:
            newrob=max(rob1+n,rob2)
            rob1=rob2
            rob2=newrob
        return rob2

        