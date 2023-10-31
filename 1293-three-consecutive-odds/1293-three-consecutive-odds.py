class Solution(object):
    def threeConsecutiveOdds(self, nums):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(nums)<=2:
            return False
        for i in range(1,len(nums)-1):
            if nums[i-1]%2!=0 and nums[i]%2!=0 and nums[i+1]%2!=0:
                return True
        return False