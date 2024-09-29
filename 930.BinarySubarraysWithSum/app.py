class solution:
    def sub(self,nums,goal):
        def help( x):        
            if x < 0:
                return 0
            l = 0
            sum = 0
            res = 0
            for r in range(len(nums)):
                sum += nums[r]
                while sum > x:
                    sum -= nums[l]
                    l+=1
                res += r-l+1
            return res
        
        
        return help(goal)- help(goal-1)
            
        
        









nums = [1,0,1,0,1]
goal = 2
solution =solution()
result = solution.sub(nums,goal)
print(result)