class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowcount=defaultdict(int)
        count=0
        for row in grid:
            rowcount[tuple(row)]+=1
        
        for col in zip(*grid):
            count+= rowcount[col]
        
        return count
        