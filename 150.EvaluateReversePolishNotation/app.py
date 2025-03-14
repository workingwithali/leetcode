def resvers(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop()+stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif c == "*":
            stack.append(stack.pop()*stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(float(b))/a)
        else:
            stack.append(int(c))
    return stack[0]
tokens = ["2","1","+","3","*"]
result = resvers(tokens)
print(result)