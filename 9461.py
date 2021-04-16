<<<<<<< HEAD
#Pn = 정삼각형의 변의 길이
#점화식 Sn=S(n-1)+S(n-5)
#DP bottom-up 방식
#이전에 계산된 값을 가지고 다음 값을 계산하도록 구현
#테스트 케이스 중 가장 큰 값까지 파도변을 구해 결과들을 리스트에 저장

t = int(input())
test_case = []
max_test_case = 0

for _ in range(t):
    n = int(input()) #n번째 정삼각형 변의 길이
    test_case.append(n)
    max_test_case = max(max_test_case,n)
rst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10,max_test_case): #??? +1 할 필요없는 이유는 인덱스가 0부터 시작되기 때문인가?  range(10,13) 10,11,12(13번째 Pn값을 의미)
    Pn = rst[i-1]+rst[i-5]
    rst.append(Pn)

for n in test_case:
    print(rst[n-1]) #nth 값은 rst[n-1]에 저장되어있다.


=======
#Pn = 정삼각형의 변의 길이
#점화식 Sn=S(n-1)+S(n-5)
#DP bottom-up 방식
#이전에 계산된 값을 가지고 다음 값을 계산하도록 구현
#테스트 케이스 중 가장 큰 값까지 파도변을 구해 결과들을 리스트에 저장

t = int(input())
test_case = []
max_test_case = 0

for _ in range(t):
    n = int(input()) #n번째 정삼각형 변의 길이
    test_case.append(n)
    max_test_case = max(max_test_case,n)
rst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10,max_test_case): #??? +1 할 필요없는 이유는 인덱스가 0부터 시작되기 때문인가?  range(10,13) 10,11,12(13번째 Pn값을 의미)
    Pn = rst[i-1]+rst[i-5]
    rst.append(Pn)

for n in test_case:
    print(rst[n-1]) #nth 값은 rst[n-1]에 저장되어있다.


>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
