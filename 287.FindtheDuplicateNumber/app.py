class solution:
    def remove(self,nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1]:
                return nums[i]
        return -1
    
solution = solution()
nums = [1,2,3,2,3,4,4]