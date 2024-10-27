class solution :
    def tem(self,t):
        n = len(t)
        res = [0]*n
        stack = []
        for i in range(n):
            while stack and t[i]>t[stack[-1]]:
                cool_day = stack.pop()
                res[cool_day] = i - cool_day
            stack[i]
        return res
solution =solution()
temperatures = [73,74,75,71,69,72,76,73]
result = solution.tem(temperatures)
