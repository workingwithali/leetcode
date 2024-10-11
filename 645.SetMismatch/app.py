class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(range(1, n + 1))
        actual_sum = sum(nums)
        total_square_sum = sum(x * x for x in range(1, n + 1))
        actual_square_sum = sum(x * x for x in nums)
        
        diff1 = total_sum - actual_sum
        diff2 = total_square_sum - actual_square_sum
        
        missing = (diff1 + (diff2 // diff1)) // 2
        duplicate = missing - diff1
        
        return [duplicate, missing]
