<<<<<<< HEAD
import sys
r=sys.stdin.readline

n = list(map(str,r().rstrip().split('-')))
nega_num = []
posi_num = 0 

for i in range(len(n)):
    n_sum = 0
    for j in list(n[i].split('+')):
        n_sum += int(j)
    if i == 0:
        posi_num += n_sum
    else:
        nega_num.append(n_sum)

print(posi_num - sum(nega_num))
=======
import sys
r=sys.stdin.readline

n = list(map(str,r().rstrip().split('-')))
nega_num = []
posi_num = 0 

for i in range(len(n)):
    n_sum = 0
    for j in list(n[i].split('+')):
        n_sum += int(j)
    if i == 0:
        posi_num += n_sum
    else:
        nega_num.append(n_sum)

print(sum(nega_num))
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
