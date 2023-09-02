class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_arr=[i for i in range(len(nums)+1)]
        return sum(new_arr)-sum(nums)
