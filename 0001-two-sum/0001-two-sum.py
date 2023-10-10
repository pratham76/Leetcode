class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #o(n2)

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return (i,j)
        """
        #o(n) soln using hashmap
        hashmap={}

        for i in range(len(nums)):
            hashmap[nums[i]]=i
        
        for i in range(len(nums)):
            c=target-nums[i]
            if c in hashmap and hashmap[c]!=i:
                return (i,hashmap[c])
        """
        hash={}
        for i,ele in enumerat(nums):
            hash[ele]=i

        for i in range(len(nums)):
            c=target-nums[i]
            if c in hash and hash[c]!=i:
                return (i,hash[c])


