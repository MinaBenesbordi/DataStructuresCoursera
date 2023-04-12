open_brackets = {"(": ")", "{": "}", "[": "]"}
close_brackets = {")", "}", "]"}

def check(open_brackets, close_brackets, str):
    stack = []
    for i, c in enumerate(str, start=1):
        if c in open_brackets:
            stack.append((c, i))
        elif c in close_brackets:
            if not stack: #If the stack is empty, we don't have an opening bracket for our closing bracket, so we return the index of the first closing bracket
                return i
            if open_brackets[stack[-1][0]] != c:
                return i
            stack.pop()
    if stack:
        return stack[-1][1]
    return "Success"

str = input()
print(check(open_brackets, close_brackets, str))
