class reverse:
    def reverse_string(self, s):
        l, r = 0 , len(s)-1
        while l < r :
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        return s

reverse = 
s = ['h','e','l','l','o']
result = reverse.reverse_string(s)
print(result)