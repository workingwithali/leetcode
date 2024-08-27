class solution :
    def parity(self,nums):
        l =0
        for r in range(len(nums)):
            if nums[r] %2 ==0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        return nums
solution = solution()
arry = [3,4,5,6,7,8,9]
result = solution.parity(arry)
print(result)