import math
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0]) # assuming all rows have the same number of columns
        dp = [ [0]*m for _ in range(n)]
        # the first row costs what it costs 
        for i in range(m):
            dp[0][i] = matrix[0][i]
        
        # now we optimize moving down taking the cheapest from the the three above
        for row in range(1,n):
            for col in range(m):
                best0 = math.inf if col == 0 else dp[row-1][col-1]
                best1 = dp[row-1][col]
                best2 = math.inf if col == m-1 else dp[row-1][col+1]
                overall_best = min(best0, best1, best2)
                dp[row][col] = matrix[row][col] + overall_best
        
        return min(dp[n-1])