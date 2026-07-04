from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        nei = [(0,1),(1,0),(-1,0),(0,-1)]

        while q:
            x,y = q.popleft()

            for dx , dy in nei:
                nx = x+dx
                ny = y + dy

                if 0<=nx<n and 0<=ny<m and grid[nx][ny] != -1:
                    if grid[nx][ny] > grid[x][y] + 1:
                        grid[nx][ny] = grid[x][y] + 1
                        q.append((nx,ny))
        
        