# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	128 MB	93871	47143	41527	51.607%
# 문제
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.



# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

# 자료 입력
a = int(input())
b = int(input())
# 문제 풀이
print(a*(b%10))
print(a*((b % 100)//10))
print(a*(b//100))
print(a*b)