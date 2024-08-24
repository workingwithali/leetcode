class solution:
    def zero(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
        return nums

solution =solution() 
arr = [1,2,3,0,0,4,5,6]
result = solution.zero(arr)
print(result)