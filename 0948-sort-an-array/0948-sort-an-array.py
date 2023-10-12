class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            left = self.sortArray(left)
            right = self.sortArray(right)

            return self.merge(left, right)
    def merge(self,list1,list2):
            res=[]
            i,j=0,0
            while i<len(list1) and j<len(list2):
                if list1[i]<list2[j]:
                    res.append(list1[i])
                    i+=1
                else:
                    res.append(list2[j])
                    j+=1
            if list1:
                res.extend(list1[i:])
            if list2:
                res.extend(list2[j:])
            return res
        
       


             


        