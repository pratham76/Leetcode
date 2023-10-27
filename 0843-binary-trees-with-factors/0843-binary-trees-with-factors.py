class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        data, mod, arr = defaultdict(int), 10**9 + 7, sorted(arr)
        for v1 in arr:
            tmp = 1
            for v2 in arr:
                if v2 >= v1:
                    break
                if v1 % v2 == 0:
                    tmp = (tmp + data[v2] * data[v1 // v2]) % mod
            data[v1] = tmp
        
        return sum(v for v in data.values()) % (10**9 + 7)