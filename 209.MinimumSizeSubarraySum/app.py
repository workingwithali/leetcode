class solution:
    def size(self,target,nums):
        l , total = 0,0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res , r-l+1)
                total -= nums[l]
                l+=1
        return 0 if res == float('inf') else res
    
sol = solution()
target = 7
nums = [2,3,1,2,4,3]
result = sol.size(target, nums)


        