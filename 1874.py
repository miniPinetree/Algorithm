import sys
sequence = list()
n = int(sys.stdin.readline())
for _ in range(n):
    sequence.append(int(sys.stdin.readline()))
    
def stack_sequence(n,sequence):
    stack = []
    num = 1
    sequence_idx = 0
    result = []

    while True:
        if len(stack)==0:
            stack.append(num)
            result.append('+')
            num += 1
        
        elif sequence[sequence_idx] == stack[-1]:
            stack.pop()
            result.append('-')
            sequence_idx +=1 #기존 idx의 수열이 충족됐기때문에 다음 idx로 넘어간다.
            if sequence_idx == n: # n = 수열을 구성하는 수의 개수
                break
        else:
            if n < num: #주어진 수열을 만들 수 없는 경우이다. (수열은 1~n 사이 수로 구성)
                print("NO")
                break
            stack.append(num)
            result.append('+')
            num +=1
    if len(stack) == 0:
        for char in result:
            print(char)


stack_sequence(n, sequence)