class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # Initialize the index for the place where the next unique element should be placed
        index = 2
        
        # Start iterating from the 3rd element (index 2)
        for i in range(2, len(nums)):
            print(nums[i])
            print(nums[index])
            # Only copy the element if it is not equal to the element two steps back
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
                
        return index
