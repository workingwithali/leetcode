class Remove:
    def dup(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l +=1
        return l

Remove = Remove()
arr=[0,0,1,1,1,2,3,4,4,4]
reault = Remove.dup(arr)
print(reault)
