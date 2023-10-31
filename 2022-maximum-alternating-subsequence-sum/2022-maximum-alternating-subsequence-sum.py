class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seven,sodd=0,0
        for i in range(len(nums)-1,-1,-1):
            tmpeven=max(sodd+nums[i],seven)
            tmpodd=max(seven-nums[i],sodd)
            seven,sodd=tmpeven,tmpodd
        
        return max(seven,sodd)
