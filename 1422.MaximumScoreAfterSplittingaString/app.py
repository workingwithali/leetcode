class solution :
    def score(self,s):
        zero = 0
        one = s.count('1')
        res = 0
        for n in range(len(s)-1):
            