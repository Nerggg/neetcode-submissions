class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col, curr_result):
            if (row < 0 or
                row >= rows or
                col < 0 or
                col >= cols or
                grid[row][col] == 0):
                return

            if grid[row][col] == 1:
                curr_result[0] += grid[row][col]
                grid[row][col] = 0

            dfs(row + 1, col, curr_result)
            dfs(row - 1, col, curr_result)
            dfs(row, col + 1, curr_result)
            dfs(row, col - 1, curr_result)

        for r in range(rows):
            for c in range(cols):
                curr = [0]
                dfs(r, c, curr)
                if curr[0] > result: result = curr[0]

        return result

