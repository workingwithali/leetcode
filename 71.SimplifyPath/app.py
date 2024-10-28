class solution:
    def paths(self,path):
        stack = []
        for i in path.split('/'):
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.' or i =='':
                