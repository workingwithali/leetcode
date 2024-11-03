class solution:
    def insert(self,nums,target):
        left, right = 0,len(nums)
        while left<=right:
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid + 1
            else:
                right = mid - 1
        return left