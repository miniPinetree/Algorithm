<<<<<<< HEAD
# 문제 : 이동경로의 수를 더한 값이 최대가 될 때 그 수를 출력해야 한다.
# 접근방식 : 
# 1. DP적용 : n은 n-1번까지 계산한 수 중 최대값과 합산하여 누적해간다.
# 2. 대각선으로 연결된 값만 선택이 가능한데 이 조건을 어떻게 구현하면 좋을까?
# 3. 삼각형 가장자리의 수들은 합산할 수 있는 선택지가 하나 뿐이다.
# 4. 대각선 이동이 가능한 것은 안쪽에 존재하는 값들이다. 
# 코드구현 :
# 1. 아래로 갈수록 1씩 증가하는 삼각형 형태의 배열 생성
# 2. 배열 인덱스는 정삼각형 모양이 아니기에 대각선 값 매칭 시 인덱스 값 지정에 유의
# 3. 삼각형 가장자리 수(리스트의 양 끝 값)는 선택지가 1개
# 4. 내부에 위치한 수는 선택지가 2개이고 그 중 큰 값을 선택하도록 조건문 설계
#
import sys

n = int(sys.stdin.readline())
#입력 값을 한 줄씩 배열에 저장
triangle_value = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

rst = []
#계산 값을 저장하기 위한 삼각형 구조 배열 생성
for i in range(1, n+1): # 내부 반복문의 범위가 되므로 1부터 시작하자.
    rst.append([0 for _ in range(i)])

for i in range(n):
    if i == 0:
        rst[0][0] = triangle_value[0][0]
    else:
        for j in range(i+1):
            #j의 위치에 따른 조건문
            if j == 0: #삼각형의 왼쪽 가장자리
                rst[i][j] = rst[i-1][j]+triangle_value[i][j]
            elif j == i: #삼각형의 오른쪽 가장자리
                rst[i][j] = rst[i-1][j-1]+triangle_value[i][j]
            else:
                rst[i][j] = max(rst[i-1][j-1],rst[i-1][j])+triangle_value[i][j]
print(max(rst[n-1]))

=======
# 문제 : 이동경로의 수를 더한 값이 최대가 될 때 그 수를 출력해야 한다.
# 접근방식 : 
# 1. DP적용 : n은 n-1번까지 계산한 수 중 최대값과 합산하여 누적해간다.
# 2. 대각선으로 연결된 값만 선택이 가능한데 이 조건을 어떻게 구현하면 좋을까?
# 3. 삼각형 가장자리의 수들은 합산할 수 있는 선택지가 하나 뿐이다.
# 4. 대각선 이동이 가능한 것은 안쪽에 존재하는 값들이다. 
# 코드구현 :
# 1. 아래로 갈수록 1씩 증가하는 삼각형 형태의 배열 생성
# 2. 배열 인덱스는 정삼각형 모양이 아니기에 대각선 값 매칭 시 인덱스 값 지정에 유의
# 3. 삼각형 가장자리 수(리스트의 양 끝 값)는 선택지가 1개
# 4. 내부에 위치한 수는 선택지가 2개이고 그 중 큰 값을 선택하도록 조건문 설계
#
import sys

n = int(sys.stdin.readline())
#입력 값을 한 줄씩 배열에 저장
triangle_value = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

rst = []
#계산 값을 저장하기 위한 삼각형 구조 배열 생성
for i in range(1, n+1): # 내부 반복문의 범위가 되므로 1부터 시작하자.
    rst.append([0 for _ in range(i)])

for i in range(n):
    if i == 0:
        rst[0][0] = triangle_value[0][0]
    else:
        for j in range(i+1):
            #j의 위치에 따른 조건문
            if j == 0: #삼각형의 왼쪽 가장자리
                rst[i][j] = rst[i-1][j]+triangle_value[i][j]
            elif j == i: #삼각형의 오른쪽 가장자리
                rst[i][j] = rst[i-1][j-1]+triangle_value[i][j]
            else:
                rst[i][j] = max(rst[i-1][j-1],rst[i-1][j])+triangle_value[i][j]
print(max(rst[n-1]))

>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
