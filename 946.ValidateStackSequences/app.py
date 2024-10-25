class solution:
    def validate(self,pushed,popped):
        stack = []
        i = 0
        for n in pushed:
            stack.append(n)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]   
solution =solution()
result = solution.validate(pushed,popped)