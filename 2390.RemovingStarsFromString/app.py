class solutin:
    def remove(self,s):
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
    
s = "leet**cod*e"
solutin = solutin()
result = solutin.remove(s)
