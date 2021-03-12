
def check_balance(string):
    stack = []

    for char in string:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")" or char =="]":
            if len(stack) == 0 :
                return False
            else:
                popped = stack.pop()
                if popped == "(" and char == ")":
                    continue
                elif popped == "[" and char == "]":
                    continue
                else:
                    return False
    return True

str = list(map(str, sys.stdin.readlines().split('.')))
while True:
    sentence = [s for s in sys.stdin.readlines]
    for row in str:
        if len(row) == 0:
            break
        elif check_balance(row):
            print('yes')
        else:
            print('no')
        str.remove(row)
