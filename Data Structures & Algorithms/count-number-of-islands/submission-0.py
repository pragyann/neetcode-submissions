class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        visited = set() # ((r,c))

        def explore(r, c):
            queue = deque([(r,c)])
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    explore(r, c)
                    islands += 1

        return islands