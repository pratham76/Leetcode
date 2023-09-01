class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for nums in grid:
            for j in range(len(nums)-1,-1,-1):
                if nums[j]<0:
                    count+=1
                else:
                    break
        return count
        