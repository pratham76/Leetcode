class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #o(n2)
        '''
        count=0
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum%k==0:
                    count+=1
        return count
        '''
        count = 0
        prefix_sum = 0
        mod_count = [0] * k
        mod_count[0] = 1  # Base case
        
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += mod_count[prefix_sum]
            mod_count[prefix_sum] += 1
            
        return count

