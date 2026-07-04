from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        visited = [[False]*m for i in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        nei = [(0,1),(1,0),(-1,0),(0,-1)]
        minute = 0

        while rotten and fresh > 0:
            l = len(rotten)

            for i in range(l):
                x , y = rotten.popleft()
                
                for dx , dy in nei:
                    nx = x+dx
                    ny = y + dy

                    if 0<=nx<n  and 0<=ny<m and grid[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        fresh -= 1
                        grid[nx][ny] = 2
                        rotten.append((nx,ny))
            minute += 1
        
        return minute if fresh == 0 else -1


