class Solution:
    def countBits(self, nums: int) -> List[int]:
        res=[]
        for i in range(nums+1):
            n=i
            count=0
            while n:
                if n%2==1:
                    count+=1
                n=n//2
            res.append(count)
        return res
            
        