class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        INF = 2147483647

        def queue_land(r, c, dist):
            if ((r < 0 or r == rows or c < 0 or c == cols) 
                or (grid[r][c] in [-1, 0] or grid[r][c] != INF)):
                return
            grid[r][c] = dist
            queue.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        dist = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                queue_land(r, c-1, dist)
                queue_land(r-1, c, dist)
                queue_land(r, c+1, dist)
                queue_land(r+1, c, dist)
            
            dist += 1