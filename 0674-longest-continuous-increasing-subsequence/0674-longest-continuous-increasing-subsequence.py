class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
            if not nums:
                return 0
            maxl,currl=1,1
            for i in range(1,len(nums)):
                if nums[i]>nums[i-1]:
                    currl+=1
                    maxl=max(maxl,currl)
                else:
                    currl=1
            return maxl
            