class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        def helper(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]!="1":
                return
            grid[r][c]="#" 
            helper(r+1,c)
            helper(r,c+1)
            helper(r-1,c)
            helper(r,c-1)
            
        if not grid: return 0
        
        count=0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1":
                    helper(i,j)
                    count+=1

        return count
        