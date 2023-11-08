class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l,r=0,0
        while r<len(nums):
            if nums[r]%2==0:
                nums[r],nums[l]=nums[l],nums[r]
                l+=1
            r+=1
        return nums