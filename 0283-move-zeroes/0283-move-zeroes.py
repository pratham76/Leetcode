class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        n=len(nums)
        while i<n:
            if nums[i]==0:
                nums.append(0)
                nums.remove(0)
            i+=1

        