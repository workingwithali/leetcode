class solution:
    def number(self, s):
        n = len(s)
        s =s+s
        alt1 = ''
        alt2 = ''
        for i in range(len(s)):
            alt1 += '1' if i%2 else '0'
            alt2 += '0' if i%2 else '1'
            