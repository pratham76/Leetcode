class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        time,fresh=0,0
        ROWS,COLS=len(grid),len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    #if fresh make it rotten
                    if row==ROWS or col==COLS or row<0 or col<0 or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        
        if fresh==0:return time
        return -1

