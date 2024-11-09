class Solution:
    def find(self, nums):
        l, r = 0, len(nums) - 1  # Set right boundary to len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:  # Compare mid with mid + 1
                l = mid + 1
            else:
                r = mid
        return l  # l and r converge to the peak element's index

solution = solution()
nums = {1,2,3,5,3,4,3,4}
r = solution.find(nums)
print(r)