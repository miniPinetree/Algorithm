## 회문문제
# 반복문에 재귀함수를 적용시켜보자

input = 'abcba'

def is_palindrome(string):
    if len(string) <=1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

    # n = len(string)//2
    # for i in range(n//2):
    #     if string[i] != string[-1-i]:
    #         return False
    # return True
    if len(string) = 1:
        return True
    if string[0] != string[-1]:
        return False
    else:
        is_palindrome(string[1:-1])

result = is_palindrome(input)
print(result)