class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0]) # x
        rows = len(grid) # y
        results = 0
        visited = set()

        def dfs(row, col):
            if (row < 0 or
                row >= rows or
                col < 0 or
                col >= cols or
                grid[row][col] == '0' or
                (row, col) in visited):
                return

            # if grid[row][col] == '1': 
                # grid[row][col] = '0'
            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    results += 1
                    dfs(r, c)

        return results
