class solution:
    def validate(self,pushed,popped):
        stack = []
        i = 0
        for n in pushed:
            stack.append(n)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i