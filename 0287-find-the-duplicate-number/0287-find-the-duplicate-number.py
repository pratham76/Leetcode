class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq=Counter(nums)
        for i in nums:
            if freq[i]>1:
                return i