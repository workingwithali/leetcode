class solutin:
    def dup (self, nums, k):
        window = set()
        l = 0
        for r in range(len(nums)):
            if r-l > k:
                window.remove(nums[l])
                l +=1
            if nums[r] in window :
                return True
            window.add(nums[r])
solutin = solutin()
nums = [1,2,4,5,3,3,5,3,2,2]
k = 4
result = solutin.dup(nums,k)
print(result)