class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash=collections.defaultdict(int)
        for i in nums:
            hash[i]+=1
        
        for i in range(len(nums)):
            if hash[nums[i]]>1:
                return True
        return False
        