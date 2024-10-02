class solution:
    def three(self,num):
        res = '0'
        for i in range(len(num)):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i:i+3])
        return '' if res == '0' else res