class solution:
    def sort(self,nums):
        l,m,h=0,0,len(nums)-1
        while m<=h:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif nums[]
