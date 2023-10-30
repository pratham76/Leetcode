class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xdiff=(coordinates[1][0]-coordinates[0][0])
        ydiff=(coordinates[1][1]-coordinates[0][1])

        for i in range(2,len(coordinates)):
            curxdiff=(coordinates[i][0]-coordinates[i-1][0])
            curydiff=(coordinates[i][1]-coordinates[i-1][1])
            if (xdiff*curydiff != ydiff*curxdiff): return False
        return True