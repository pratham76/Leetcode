class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        re=[]
        max_val=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_val:
                re.append(True)
            else:
                re.append(False)
        return re
