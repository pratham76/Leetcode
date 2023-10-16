class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        previous=self.getRow(rowIndex-1)
        row=[1]
        for i in range(1,len(previous)):
            row.append(previous[i-1]+previous[i])
        row.append(1)
        return row
        