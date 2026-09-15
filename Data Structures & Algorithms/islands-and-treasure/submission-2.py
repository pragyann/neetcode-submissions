class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def append_to_queue(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols) or ((r, c) in visited) or grid[r][c] == -1:
                return
            queue.append((r,c))
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        dist = 0
        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                r, c = queue.popleft()

                grid[r][c] = dist

                append_to_queue(r + 1, c)
                append_to_queue(r - 1, c)
                append_to_queue(r, c + 1)
                append_to_queue(r, c - 1)
            
            dist += 1
            


