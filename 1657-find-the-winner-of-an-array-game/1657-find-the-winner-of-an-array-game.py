class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner=arr[0]
        wincount=0
        for i in range(1,len(arr)):
            if arr[i]<winner:
                wincount+=1
            elif arr[i]>winner:
                winner=arr[i]
                wincount=1
            if wincount==k:
                return winner
        return winner

            
