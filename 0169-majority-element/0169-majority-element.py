class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seq=dict()
        for i in nums:
            if i not in seq.keys():
                seq[i]=1
            else:
                seq[i]+=1
        for i in seq.keys():
            if seq[i]>len(nums)/2:
                return i;    
        
