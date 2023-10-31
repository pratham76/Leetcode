class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        l,s=len(mat),0
        for i in range(l):
            if i==l-i-1:
                s+=mat[i][i]
            else:
                s+=mat[i][i]+mat[i][l-i-1] 
        return s