class solution:
    def sign(self,nums):
        sign = 1
        for i in nums:
            if i == 0:
                return 0
            elif i<0:
                sign = -sign
        return sign
 