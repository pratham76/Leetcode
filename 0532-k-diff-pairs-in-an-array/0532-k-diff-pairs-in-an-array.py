class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        hashmap = {}
        for i, ele in enumerate(nums):
            hashmap[ele] = i
        print(hashmap)
        for i in range(len(nums)):
            dif = nums[i] - k
            if dif in hashmap and hashmap[dif] != i and hashmap[dif] is not None:
                count += 1
                hashmap[dif] = None  # Mark the second element as used to avoid duplicates
        return count
