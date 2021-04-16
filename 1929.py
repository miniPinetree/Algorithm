<<<<<<< HEAD
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

#접근방식
#약수의 법칙을 이용해 N의 제곱근보다 작은 소수로 나누었을 때와
#소수판별 중 시간적으로 효율적이라 하는 에라토스테네스의 체를 비교해봄
#에라토스테네스의 체는 시간복잡도가 매우 빠르나 메모리가 많이 필요하다는 단점이 있다.

#문제풀이
import math

M,N= map(int, input().split())
array = [True for i in range(N+1)]

for i in range(2,int(math.sqrt(N))+1):
    if array[i] == True: #제거되지 않은 숫자인가를 판별함.
        j = 2 #j는 제거되지 않은 가장 작은 수를 의미함.
        while i*j <= N:
            array[i*j] = False #j의 배수는 소수가 아니다.
            j+=1 #j의 배수를 다 제거하고나면 그 다음으로 작은 수로 넘어간다.

for i in range(M, N+1): #입력값 범위 내에서만 출력되도록 지정
    if array[i] and i!=1: #1은 소수가 아니므로 제외해주는 조건
        print(i)
# def prime_num(a):
#     if a<2:
#         return False
#     else:
#         for i in range(2,a):
#             if a%i ==0:
#                 return False
#         return True

# p_num = [2,3,5,7]
# ans = []

# for i in range(1, N+1):
#     for j in p_num:
#         i%j == 0
#     ans.append(6*n-1)
#     ans.append(6*n+1)
# for i in ans:
#     # print(i)
#     for j in p_num:
#         # print(j)
#         if i%j == 0:
#             ans.remove(i)
# # print(ans)

# # for num in p_num:
# #     if num >= M:
# #         print(num)
# # for ans in ans:
# #     if ans <= N:
# #         print(ans)


=======
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

#접근방식
#약수의 법칙을 이용해 N의 제곱근보다 작은 소수로 나누었을 때와
#소수판별 중 시간적으로 효율적이라 하는 에라토스테네스의 체를 비교해봄
#에라토스테네스의 체는 시간복잡도가 매우 빠르나 메모리가 많이 필요하다는 단점이 있다.

#문제풀이
import math

M,N= map(int, input().split())
array = [True for i in range(N+1)]

for i in range(2,int(math.sqrt(N))+1):
    if array[i] == True: #제거되지 않은 숫자인가를 판별함.
        j = 2 #j는 제거되지 않은 가장 작은 수를 의미함.
        while i*j <= N:
            array[i*j] = False #j의 배수는 소수가 아니다.
            j+=1 #j의 배수를 다 제거하고나면 그 다음으로 작은 수로 넘어간다.

for i in range(M, N+1): #입력값 범위 내에서만 출력되도록 지정
    if array[i] and i!=1: #1은 소수가 아니므로 제외해주는 조건
        print(i)
# def prime_num(a):
#     if a<2:
#         return False
#     else:
#         for i in range(2,a):
#             if a%i ==0:
#                 return False
#         return True

# p_num = [2,3,5,7]
# ans = []

# for i in range(1, N+1):
#     for j in p_num:
#         i%j == 0
#     ans.append(6*n-1)
#     ans.append(6*n+1)
# for i in ans:
#     # print(i)
#     for j in p_num:
#         # print(j)
#         if i%j == 0:
#             ans.remove(i)
# # print(ans)

# # for num in p_num:
# #     if num >= M:
# #         print(num)
# # for ans in ans:
# #     if ans <= N:
# #         print(ans)


>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
