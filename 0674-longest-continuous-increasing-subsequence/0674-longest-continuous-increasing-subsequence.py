class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
            if not nums:
                return 0

            res = 1  # Initialize with 1 because the minimum length is 1.
            current_length = 1  # Initialize with 1 because we have at least one element in the array.

            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    current_length += 1
                    res = max(res, current_length)
                else:
                    current_length = 1  # Reset the length when the sequence is not increasing.

            return res
            