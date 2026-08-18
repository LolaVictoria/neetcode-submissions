class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in range(len(matrix)):
            left, right = 0, len(matrix[row]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
            


        