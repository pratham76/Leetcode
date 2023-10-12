class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N=len(grid)
        queue=deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c]==1:
                    queue.append([r,c])
        res=-1
        direct=[[0,1],[1,0],[0,-1],[-1,0]]
        while queue:
            r,c=queue.popleft()
            res=grid[r][c]
            for dr,dc in direct:
                nr,nc=r+dr,c+dc
                if max(nr,nc)<N and min(nr,nc)>=0 and grid[nr][nc]==0:
                    queue.append([nr,nc])
                    grid[nr][nc]=grid[r][c]+1
        
        return res-1 if res>1 else -1
        