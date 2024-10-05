class solution:
    def Product(self,nums):
        max1 = max2 = 0
        min1 = min2 = float("inf")
        for n in nums:
            if n > max2:
                if n > max1:
                    max1 , max2 = n , max1
                else:
                    max2 = n
            if n < min2:
                if n < min1:
                    min1 , min2 = n , min1
                else:
                    min2 = n

        return (max1*max2)-(min1*min2)
nums = [5,6,2,7,4]
solution = solution()
result = solution.Product(nums)
print(result)