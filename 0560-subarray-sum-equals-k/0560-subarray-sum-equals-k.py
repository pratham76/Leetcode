class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #o(n2)
        '''
        n=len(nums)
        count=0
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                if sum==k:
                    count+=1
        return count
        '''
        #o(n) time and o(n) space

        res=0
        cursum=0
        prefixsum={0:1}
        for n in nums:
            cursum+=n
            res+=prefixsum.get(cursum-k,0)
            prefixsum[cursum]=1+prefixsum.get(cursum,0)
        return res