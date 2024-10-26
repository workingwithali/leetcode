class solution:
    def collision(self, asteroid):
        stack = []
        for s in asteroid:
            while stack and s < 0 and stack[-1] > 0:
                diff = s + stack[-1]
                if diff > 0:
                    s == 0
                elif diff < 0:
                    stack.pop()
                else:
                    s = 0
                    stack.pop()
            if s:
                stack.append(s)
            