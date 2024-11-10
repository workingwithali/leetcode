class solution:
    def d(self,matrix,target):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False
    
solution =solution()
