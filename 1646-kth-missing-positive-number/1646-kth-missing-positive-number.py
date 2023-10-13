class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        num = 1

        while missing_count < k:
            if num not in arr:
                missing_count += 1
                if missing_count == k:
                    return num
            num += 1

        return -1  # This line should not be reached if k is valid.
                

