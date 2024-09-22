class solution:
    def number(self, s):
        n = len(s)
        s =s+s
        alt1 = ''
        alt2 = ''
        for i in range(len(s)):
            alt1 += '1' if i%2 else '0'
            alt2 += '0' if i%2 else '1'
        res = len(s)
        d1 ,d2 = 0 ,0
        l = 0
        for r in range(len(s)):
            if s[r] != alt1[r]:
                d1 +=1
            if s[r] != alt2[r]:
                d2 +=1

            if (r-l+1) > n:
                if s[l] != alt1[l]:
                    d1 -=1
                if s[l] != alt2[l]:
                    d2 -=1
                l+=1
            if (r-l+1)== n:
                res = min(res,d1,d2)
        return res
    
solution = solution()
s = "111000"
result = solution.number(s)
print(result)
            
