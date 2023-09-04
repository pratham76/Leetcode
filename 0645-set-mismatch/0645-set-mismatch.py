class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[]
        s=set(range(1,len(nums)+1))
        l.append(mode(nums))
        l.append((list(s-set(nums)))[0])
        return l