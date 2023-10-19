class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS,COLS=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]!="1":
                return
            grid[r][c]="#"
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        count=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count

        