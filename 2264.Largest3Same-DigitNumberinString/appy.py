class solution:
    def three(self,num):
        res = '0'
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i:i+3])
        return '' if res == '0' else res
    
num = "6777133339"
solution = solution()
result = solution.three(num)
print(result)