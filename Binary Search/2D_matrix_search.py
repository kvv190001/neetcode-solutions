class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r = int(m / 2)
        c = int(n / 2)

        if target < matrix[0][0]:
            return False
        if target > matrix[m-1][n-1]:
            return False

        while True:
            if matrix[r][0] == target:
                return True
            elif matrix[r][0] < target and r == m-1:
                break
            elif matrix[r][0] < target and matrix[r+1][0] > target:
                break
            elif matrix[r][0] < target:
                r = int((r+m)/2)
            elif matrix[r][0] > target:
                r = int(r/2)
            else:
                return False
        while True:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target and c == n-1:
                return False
            elif matrix[r][c] > target and c == 0:
                return False
            elif matrix[r][c] < target and matrix[r][c+1] > target:
                return False
            elif matrix[r][c] < target:
                c = int((c+n)/2)
            elif matrix[r][c] > target:
                c = int(c/2)
            else:
                return False