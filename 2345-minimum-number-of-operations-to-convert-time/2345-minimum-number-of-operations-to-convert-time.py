class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        count=0
        def f(t):
            hh,mm=list(map(int,t.split(':')))
            return hh*60+mm
        
        left=f(correct)-f(current)
        for t in [60,15,5,1]:
            while left>=t:
                left-=t
                count+=1
        return count

        