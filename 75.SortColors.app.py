class solution:
    def sort(self,nums):
        l,m,h=0,0,len(nums)-1
        while m<=h:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif nums[m]==1:
                mid+=1
            else:
                nums[l],nums[h]=nums[h],nums[l]
                h-=1
solution =solution()
nums = {0,2,1,2,0}
r =solution.sort(nums)
