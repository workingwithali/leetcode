class solution:
    def equat(self,s,t,maxCost):
        curCost = 0
        l = 0
        res = 0
        for r in range(len(s)):
            curCost += abs(ord(s[r])-ord(t[r]))
            while curCost > maxCost:
                curCost -= abs(ord(s[l])-ord(t[l]))
                l+=1
            res = max(res, r-l+1)
        return res
s = "abcd"
t = "bcdf"
maxCost = 3
solution = solution()
result = solution.equat(s,t,maxCost)
print(result)