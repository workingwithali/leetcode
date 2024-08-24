class solution:
    def zero(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1

solution =solution() 