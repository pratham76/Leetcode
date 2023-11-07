class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minreach=[]
        for d,s in zip(dist,speed):
            minute=math.ceil(d/s)
            minreach.append(minute)
        
        minreach.sort()
        res=0
        for mint in range(len(minreach)):
            if mint>=minreach[mint]:
                return res
            res+=1

        return res 