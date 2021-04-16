<<<<<<< HEAD
n = int(input())
arr = [0]*n #체스판 생성, 행/열이 겹치지 않기에 1차원 배열로도 구현 가능하다.
con1_column = [0]*n #같은 열에 존재하는 지
con2_upward_diagonal = [0]*(2*n-1) #우상향 대각선에 존재하는 지
con3_downward_diagonal = [0]*(2*n-1) #우하향 대각선에 존재하는 지
cnt=0 #

def queen(i):
    global cnt
    for j in range(n):
        if (not con1_column[j] and not con2_upward_diagonal[i+j] and not con3_downward_diagonal[i-j+n-1]):
            arr[i] = j #가로, 세로, 대각선 모두 겹치지 않는다면 arr에 저장한다.
            if i==(n-1): #마지막 행까지 퀸을 놓았다면
                cnt+=1 #경우의 수를 하나 증가시킨다.
            else:
                con1_column[j] = con2_upward_diagonal[i+j] = con3_downward_diagonal[i-j+n-1] =1
                queen(i+1)
                con1_column[j] = con2_upward_diagonal[i+j] = con3_downward_diagonal[i-j+n-1] =0
    return cnt
queen(0)
print(cnt)




=======
n = int(input())
arr = [0]*n #체스판 생성, 행/열이 겹치지 않기에 1차원 배열로도 구현 가능하다.
con1_column = [0]*n #같은 열에 존재하는 지
con2_upward_diagonal = [0]*(2*n-1) #우상향 대각선에 존재하는 지
con3_downward_diagonal = [0]*(2*n-1) #우하향 대각선에 존재하는 지
cnt=0 #

def queen(i):
    global cnt
    for j in range(n):
        if (not con1_column[j] and not con2_upward_diagonal[i+j] and not con3_downward_diagonal[i-j+n-1]):
            arr[i] = j #가로, 세로, 대각선 모두 겹치지 않는다면 arr에 저장한다.
            if i==(n-1): #마지막 행까지 퀸을 놓았다면
                cnt+=1 #경우의 수를 하나 증가시킨다.
            else:
                con1_column[j] = con2_upward_diagonal[i+j] = con3_downward_diagonal[i-j+n-1] =1
                queen(i+1)
                con1_column[j] = con2_upward_diagonal[i+j] = con3_downward_diagonal[i-j+n-1] =0
    return cnt
queen(0)
print(cnt)




>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
