class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        
        max_val=-1
        for i in range(len(arr)-1,-1,-1):
            curr_ele=arr[i]
            arr[i]=max_val
            max_val=max(max_val,curr_ele)
        
        return arr
        