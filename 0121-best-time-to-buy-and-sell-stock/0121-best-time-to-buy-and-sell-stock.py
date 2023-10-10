class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #o(n2)
        '''
        maxp=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                maxp=max(maxp,prices[j]-prices[i])
        return maxp
        '''

        #o(n)

        minp=prices[0]
        maxp=0
        for i in range(1,len(prices)):
            maxp=max(maxp,prices[i]-minp)
            minp=min(minp,prices[i])
        return maxp



      
           

