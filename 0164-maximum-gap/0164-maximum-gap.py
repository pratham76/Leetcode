class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxd=0
        for i in range(len(nums)-1):
            maxd=max(maxd,abs(nums[i+1]-nums[i]))
        
        return maxd
