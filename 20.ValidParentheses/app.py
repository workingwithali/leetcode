class solutin :
    def vaild(self,s):
        stack =[]
        cto ={")":"(","]":"[","}":"{}"}
        for c in s:
            if c in cto:
                if stack and stack[-1]