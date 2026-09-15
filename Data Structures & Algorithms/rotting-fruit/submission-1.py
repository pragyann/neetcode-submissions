class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()

        time, fresh = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    adj_r, adj_c = r + dr, c + dc

                    if (adj_r >= 0 and adj_r < rows and adj_c >=0 and adj_c < cols) and grid[adj_r][adj_c] == 1:
                        grid[adj_r][adj_c] = 2
                        fresh -= 1
                        queue.append((adj_r,adj_c))
            time += 1

        return time if fresh == 0 else -1