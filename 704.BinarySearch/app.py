class solution :
    def binary(self, nums,target):
        left, right = 0 ,len(nums)
        while left<=right:
            mid= (right+left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid +1
            else:
                right = mid -1
        return -1
    
solution = solution()
nums = [-1,0,3,5,9,12], target = 9
result = solution.binary(nums,target)
print(result)
