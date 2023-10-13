class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2

            # If the mid element is greater than the element to its right,
            # a peak must exist on the left side.
            if nums[mid] > nums[mid + 1]:
                right = mid
            # Otherwise, a peak must exist on the right side.
            else:
                left = mid + 1

        return left
            