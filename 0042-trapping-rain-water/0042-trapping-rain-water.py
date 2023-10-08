class Solution:
    def trap(self, height: List[int]) -> int:
        #water holded by the h[i]= min(max(l),max(R))-h[i]
        #my solution
        """
        sum=0
        for i in range(len(height)):
            if i == 0:
                maxl=0
            else:
                maxl = max(height[:i])
            if i == len(height)-1:
                maxr=0
            else:
                maxr=max(height[i+1:])
            sum+=max(min(maxl,maxr)-height[i],0)

        return sum

        
        l,r=0,len(height)-1
        lmax,rmax=height[l],height[r]
        res=0
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,height[l])
                res+=lmax -height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                res+=rmax-height[r]
        return res
        """

        l,r=0,len(height)-1
        lmax,rmax=height[l],height[r]
        res=0
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,height[l])
                res+=lmax-height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                res+=rmax-height[r]
        return res

            

