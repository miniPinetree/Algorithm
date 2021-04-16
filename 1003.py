<<<<<<< HEAD

# 접근방식
# 호출횟수를 메모이제이션한 다음
# 호출횟수도 피보나치 수열처럼 계산해보자

memo = {
0: [1, 0],
1: [0 ,1],
2: [1, 1]
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    
    nth_fibo_zero = fibo_dynamic_programming(n-1, fibo_memo)[0] + fibo_dynamic_programming(n-2, fibo_memo)[0]
    nth_fibo_one = fibo_dynamic_programming(n-1, fibo_memo)[1] + fibo_dynamic_programming(n-2, fibo_memo)[1]
    fibo_memo[n] = [nth_fibo_zero, nth_fibo_one]
    return fibo_memo[n]

t = int(input())
for _ in range(t):
    n = int(input())
    result = fibo_dynamic_programming(n, memo)
    print(result[0],result[1])

=======

# 접근방식
# 호출횟수를 메모이제이션한 다음
# 호출횟수도 피보나치 수열처럼 계산해보자

memo = {
0: [1, 0],
1: [0 ,1],
2: [1, 1]
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    
    nth_fibo_zero = fibo_dynamic_programming(n-1, fibo_memo)[0] + fibo_dynamic_programming(n-2, fibo_memo)[0]
    nth_fibo_one = fibo_dynamic_programming(n-1, fibo_memo)[1] + fibo_dynamic_programming(n-2, fibo_memo)[1]
    fibo_memo[n] = [nth_fibo_zero, nth_fibo_one]
    return fibo_memo[n]

t = int(input())
for _ in range(t):
    n = int(input())
    result = fibo_dynamic_programming(n, memo)
    print(result[0],result[1])

>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
