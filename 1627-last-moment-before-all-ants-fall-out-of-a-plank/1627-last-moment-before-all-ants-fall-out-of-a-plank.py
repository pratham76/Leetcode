class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(n-min(right,default=float("inf")),max(left,default=float("-inf")))