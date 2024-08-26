class solution:
    def string(self,words):
        for w in words:
            l, r = 0 ,len(w)-1
            while w[l] == w[r]:
                if l >= r:
                    return w
                l +=1
                r -=1
        return ""
    
solution = solution()
arr = ['adfa', 'ads','aba','ere' ]
result = solution.string(arr)
print(result)

