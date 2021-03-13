import sys
r=sys.stdin.readline

n = int(r())
card_list = sorted(list(map(int,r().split())))
m = int(r())
num_list = list(map(int,r().split()))

def is_existing_target_number_binary(target, array):
    start_index=0
    end_index=len(array)-1
    mid_index=(start_index+end_index)//2

    while start_index<=end_index:
        if array[mid_index] == target:
            return True
        elif array[mid_index] > target:
            end_index = mid_index -1
        else:
            start_index = mid_index +1
        mid_index=(start_index+end_index)//2

    return False

ans = []
for num in num_list:
    if is_existing_target_number_binary(num,card_list):
        ans.append(1)
    else:
        ans.append(0)
for i in range(len(ans)):
    print(ans[i], end =  ' ')

