class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                adj_r, adj_c = r + dr, c + dc

                if (adj_r >= 0 and adj_r < rows and adj_c >=0 and adj_c < cols) and grid[adj_r][adj_c] == 2147483647:
                    print("updating dist")
                    grid[adj_r][adj_c] = grid[r][c] + 1
                    queue.append((adj_r, adj_c))