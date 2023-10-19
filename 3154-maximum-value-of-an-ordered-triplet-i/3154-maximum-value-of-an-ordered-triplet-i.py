class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
         pref = accumulate(nums, max)
         suff = list(accumulate(nums[::-1], max))[::-1]

         return max(0,*((J-I) * K for I, J, K in zip(nums[1:],pref,suff[2:])))