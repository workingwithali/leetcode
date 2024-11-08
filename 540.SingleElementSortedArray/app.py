def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        # Ensure `mid` is even for comparison consistency
        if mid % 2 == 1:
            mid -= 1
        print(mid)
        
        if nums[mid] == nums[mid + 1]:
            # Single element is in the right half
            left = mid + 2
        else:
            # Single element is in the left half
            right = mid
    
    return nums[left]

# Example usage
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8,9]
print(singleNonDuplicate(nums))  # Output: 2
