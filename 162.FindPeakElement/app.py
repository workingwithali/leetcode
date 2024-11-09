class solution:
    def find(self,nums):
        l,r=0,len(nums)
        while l<r:
            mid = (r+l)//2
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r=mid
        return l
solution =solution()
nums = {1,2,3,5,3,4,3,4}
s