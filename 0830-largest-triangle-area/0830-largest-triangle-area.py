from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        def area(x1, y1, x2, y2, x3, y3):
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
        max_area = 0.0

        for i, j, k in combinations(points, 3):
            x1, y1 = i
            x2, y2 = j
            x3, y3 = k
            max_area = max(max_area, area(x1, y1, x2, y2, x3, y3))

        return max_area