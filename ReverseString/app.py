class solution:
    def resverse(self, s)
        s = list(s)
        l = 0
        for r in range(len(s)):
            if s[r] == " " or r == len(s)-1:
                tr = r - 1 if s[r] == " " else r
                while l < tr:
                    s[l], s[]