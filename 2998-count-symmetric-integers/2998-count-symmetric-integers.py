class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            numstr=str(i)
            if len(numstr)//2==len(numstr)/2:
                l,r=0,len(numstr)-1
                ls,rs=0,0
                while l <= len(numstr) // 2 and r >= len(numstr) // 2:
                    ls+=int(numstr[l])
                    rs+=int(numstr[r])
                    l+=1
                    r-=1
                if ls==rs:
                    count+=1
        return count


                    
