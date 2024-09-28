class solution:
    def equat(self,s,t,maxCost):
        curCost = 0
        l = 0
        res = 0
        for r in range(len(s)):
            curCost += abs(ord(s[r])-ord(t[s]))
            while curCost > maxCost:
                curCost -= abs(ord(s[l])-ord(t[l]))
            res = max(res, r-l+1)
        return res
    