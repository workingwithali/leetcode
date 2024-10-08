class solultion:
    def change(self,s):
        count = 0
        for n in range(len(s)):
            if n % 2:
                count += 1 if s[n] =='0' else 0
            else:
                count += 1 if s[n] == '1' else 
        return min(count, len(s)-count)
s = "0100"
solultion = solultion()
result = solultion.change(s)
print(result)