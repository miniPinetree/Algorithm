import sys

from collections import Counter

r=sys.stdin.readline

n=int(r())
num_list =[]

for _ in range(n):
    num = int(r())
    num_list.append(num)

num_list.sort()

mode = Counter(num_list).most_common(2) 

print(round(sum(num_list)/len(num_list)))
print(num_list[len(num_list)//2])
print(mode[1][0] if len(mode)>1 and mode[0][1]==mode[1][1] else mode[0][0])
print(num_list[-1]-num_list[0])

