class solution:
    def d(self,matrix,target):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False
    
solution =solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
result = solution.d(matrix,target)