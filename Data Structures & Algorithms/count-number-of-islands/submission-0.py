class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0]) # x
        rows = len(grid) # y
        results = 0

        def dfs(row, col):
            if (row < 0 or
                row >= rows or
                col < 0 or
                col >= cols or
                grid[row][col] == '0'):
                return

            if grid[row][col] == '1': grid[row][col] = '0'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    results += 1
                    dfs(r, c)

        return results
