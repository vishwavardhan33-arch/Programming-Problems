class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minute = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        if len(q)==0:
            return -1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                r = curr[0]
                c = curr[1]
                for d in directions:
                    nr = r+d[0]
                    nc = c+d[1]
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc]=2
                        q.append([nr,nc])
                        fresh-=1
            if q:
                minute+=1
        if fresh==0:
            return minute
        return -1
        