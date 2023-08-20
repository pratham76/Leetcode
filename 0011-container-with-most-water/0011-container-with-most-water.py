class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Brute fore
        res=0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                area=(j-i)*(min(height[j],height[i]))
                res=max(res,area)
        return res
        """
        #O(N)
        l,r=0,len(height)-1
        max_area=0
        while l<r:
            area=(r-l)*min(height[r],height[l])
            max_area=max(area,max_area)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        
        return max_area

        


