class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res=[1]*len(nums)
        pre,pos=1,1
        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i]*=pos
            pos*=nums[i]
        
        return res
