s = "()()"
stack = []  
pairs = {')': '(', '}': '{', ']': '['}  

for char in s:
    if char in "({[":  
        stack.append(char)
    else:  
        if not stack:  
            print("False")
            break
        if stack[-1] == pairs[char]: 
            stack.pop()  
        else:
            print("False")  
            break

if len(stack) == 0:
    print("True")
