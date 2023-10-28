class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        vs = [v for v in Counter(arr).values()]
        return len(vs)==len(set(vs))