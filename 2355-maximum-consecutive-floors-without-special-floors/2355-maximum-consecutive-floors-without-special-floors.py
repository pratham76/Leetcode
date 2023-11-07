class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        res = max((b-a-1 for a, b in pairwise(special)), default = 0)

        return max(res, special[0] - bottom, top - special[-1])