class solution:
    def size(target,nums):
        l , total = 0,0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res , r-l+1)
                total -= nums[l]
                l+=1
        return 0 if res == float('int') else res
    
solution = solution()


        