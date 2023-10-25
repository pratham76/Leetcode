class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])

        return self.merge(left,right)

    def merge(self,left,right):
        res=[]
        i,j=0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        
        if i<len(left):
            res.extend(left[i:])
        if j<len(right):
            res.extend(right[j:])
        
        return res
    
