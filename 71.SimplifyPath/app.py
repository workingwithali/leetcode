class solution:
    def paths(self,path):
        stack = []
        for i in path.split('/'):
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.' or i =='':
                continue
            else:
                stack.append(i)
        return '/'+'/'.join(stack)
solution =solution()
path = "//home/./user//document/../file"
result = solution.paths(path)
print(result)