class solution :
    def water(self, height):
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = r-l * min(height[l], height[r])
            res = max(area,res)
            if height[l] < height[r]:
                l +=1
            else: 
                r -=1
        return res
    
height = [2,3,5,7,9,3,5,10,]
solution = solution()
result = solution.water(height)
print(result)

