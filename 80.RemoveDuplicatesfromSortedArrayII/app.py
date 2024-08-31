class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)        
        l = 2        
        for r in range(2, len(nums)):
            
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1                
        return l
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
length = solution.removeDuplicates(nums)

print("Length of array after removing duplicates:", length)
print("Modified array:", nums[:length])
