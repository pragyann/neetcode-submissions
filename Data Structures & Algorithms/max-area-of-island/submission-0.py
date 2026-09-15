class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def explore(r, c):
            area = 1
            stack = [(r,c)]
            visited.add((r,c))

            while stack:
                row, col = stack.pop()
                directions = [[1,0], [-1, 0], [0, 1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and c in range(cols)
                        and grid[r][c] == 1 and (r,c) not in visited):
                        area += 1
                        stack.append((r,c))
                        visited.add((r,c))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    print("exploring")
                    area = explore(r,c)
                    max_area = max(area, max_area)

        return max_area