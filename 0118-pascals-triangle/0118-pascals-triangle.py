class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
       nums=[]
       nums.append([1])
       for i in range(numRows-1):
           newrow=[1]
           for j in range(i):
               newrow.append(nums[i][j]+nums[i][j+1])
           newrow.append(1)
           nums.append(newrow)
       return nums
        
         