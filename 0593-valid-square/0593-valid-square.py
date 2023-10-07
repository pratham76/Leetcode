class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1==p2==p3==p4:
            return False
        def dist(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        distances = [
            dist(p1, p2),
            dist(p1, p3),
            dist(p1, p4),
            dist(p2, p3),
            dist(p2, p4),
            dist(p3, p4)
        ]
        
        # Sort the distances in ascending order
        distances.sort()
        
        # Check if the first four distances are equal (sides of a square),
        # and the last two distances are equal (diagonals of a square)
        return distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]
    