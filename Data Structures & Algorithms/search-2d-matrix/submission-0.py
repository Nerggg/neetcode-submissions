class Solution:
    def calcMid(self, matrix, left, right):
        # left and right is [row, col]
        col_length = len(matrix[0])
        linearized_left = col_length * left[0] + left[1]
        linearized_right = col_length * right[0] + right[1]

        mid = linearized_left + (linearized_right - linearized_left) // 2

        mid_row = mid // col_length
        mid_col = mid % col_length
        
        return matrix[mid_row][mid_col], mid


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = [0, 0]
        right = [len(matrix) - 1, len(matrix[0]) - 1]
        col_length = len(matrix[0])

        while (col_length * left[0] + left[1]) <= (col_length * right[0] + right[1]):
            mid_val, mid_idx = self.calcMid(matrix, left, right)
            # print(f"mid_val: ", mid_val)

            if mid_val == target: return True
            elif mid_val < target: 
                mid_idx += 1
                left[0], left[1] = mid_idx // col_length, mid_idx % col_length
            elif mid_val > target: 
                mid_idx -= 1
                right[0], right[1] = mid_idx // col_length, mid_idx % col_length

        return False
