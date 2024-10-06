class solution :
    def score(self,s):
        zero = 0
        one = s.count('1')
        res = 0
        for n in range(len(s)-1):
            if s[n] == "0":
                zero += 1
            else:
                one -=1
            res = max(res , zero + one)
        return res

solution = solution()
