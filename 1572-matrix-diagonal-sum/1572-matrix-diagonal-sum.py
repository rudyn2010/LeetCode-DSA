class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        
        for i in range(n):
            #add values from primary diagonal 
            res += mat[i][i] 
            
            #add values from secondary diagonal 
            res += mat[i][len(mat) - 1 - i]
            
        #subtract overlapping middle value from both diagonals if necessary; use of ternary
        return res - (mat[n // 2][n // 2] if n % 2 else 0)