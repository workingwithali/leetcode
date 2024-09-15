class solutin :
    def vaild(self,s):
        stack =[]
        cto ={")":"(","]":"[","}":"{"}
        for c in s:
            if c in cto:
                if stack and stack[-1] == cto[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
solutin = solutin()
s = "()[]{}"
result = solutin.vaild(s)
print(result)