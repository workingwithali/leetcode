class solution:
    def resverse(self, s):
        s = list(s)
        l = 0
        for r in range(len(s)):
            if s[r] == " " or r == len(s)-1:
                tr = r - 1 if s[r] == " " else r
                while l < tr:
                    s[l], s[tr] = s[tr], s[l]
                    l +=1
                    r -=1
                l = r +1
        return ''.join(s)
solution = solution()
s = "ali is good boy"
result =