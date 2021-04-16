<<<<<<< HEAD
c = int(input())
ans = []

for _ in range(c):
    score_list = list(map(int, input().split()))
    avg = sum(score_list[1:])/score_list[0]
    above_avg_student_num = 0
    for score in score_list[1:]:
        if score > avg:
            above_avg_student_num+=1
    above_avg_student_rate = above_avg_student_num/score_list[0]*100
    ans.append(above_avg_student_rate)

for a in ans:
=======
c = int(input())
ans = []

for _ in range(c):
    score_list = list(map(int, input().split()))
    avg = sum(score_list[1:])/score_list[0]
    above_avg_student_num = 0
    for score in score_list[1:]:
        if score > avg:
            above_avg_student_num+=1
    above_avg_student_rate = above_avg_student_num/score_list[0]*100
    ans.append(above_avg_student_rate)

for a in ans:
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
    print(format(a,".3f")+'%')