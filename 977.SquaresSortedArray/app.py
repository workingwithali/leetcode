class solution:
    def saquare(self,nums):
        n = len(nums)
        result = [0]*n
        l, r = 0, n-1
        position = n-1
        while l<=r:
            left_saq = nums[l]**2
            right_saq = nums[r]**2
            if left_saq > right_saq:
                result[position] = left_saq
                l+=1
            else:
                result[position] = right_saq
                r-=1
            position -=1
        return result
