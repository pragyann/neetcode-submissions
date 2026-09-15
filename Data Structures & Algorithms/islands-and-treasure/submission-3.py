class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        rows, cols = len(grid), len(grid[0])

        def append_to_queue(r,c,d):
            if (r < 0 or r == rows or c < 0 or c == cols) or grid[r][c] in [-1, 0] or grid[r][c] != 2147483647:
                return
            grid[r][c] = dist
            queue.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        dist = 1
        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                r, c = queue.popleft()

                append_to_queue(r + 1, c, dist)
                append_to_queue(r - 1, c, dist)
                append_to_queue(r, c + 1, dist)
                append_to_queue(r, c - 1, dist)
            
            dist += 1
            


