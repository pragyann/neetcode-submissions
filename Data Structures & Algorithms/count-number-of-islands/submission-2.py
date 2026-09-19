class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set() # (r, c)

        rows, cols = len(grid), len(grid[0])

        def explore(r, c):
            stack = [(r,c)]
            visited.add((r,c))

            while stack:
                row, col = stack.pop()

                for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and c in range(cols)) and\
                        ((r, c) not in visited) and\
                        (grid[r][c] == "1"):
                        stack.append((r, c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    explore(r, c)
                    islands += 1 

        return islands