class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        cnt = 0
        for i, j, k in itertools.combinations(arr, 3):
            if abs(i-j) <= a and abs(j-k) <= b and abs(k-i) <= c:
                cnt +=1
        return cnt