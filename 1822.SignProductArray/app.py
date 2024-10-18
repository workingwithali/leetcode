class solution:
    def sign(self,nums):
        sign = 1
        for i in nums:
            if i == 0:
                return 0
            elif i<0:
                sign = -sign
        return sign


solution = solution()
nums = [2,3,4,-3,-3,-4,-4]
result = solution.sign(nums)
