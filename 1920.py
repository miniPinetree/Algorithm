import sys
r = sys.stdin.readline
n=int(r())
ns = sorted(list(map(int,r().split())))
m = int(r())
ms = list(map(int,r().split()))

def is_existing_target_number_binary(target,array):
    start_index=0
    end_index=len(array)-1
    mid_index=(start_index+end_index)//2

    while start_index<=end_index:
        if array[mid_index] == target:
            return 1
        elif array[mid_index] > target:
            end_index = mid_index -1
        else:
            start_index = mid_index +1
        mid_index=(start_index+end_index)//2

    return 0

for m in ms:
    print(is_existing_target_number_binary(m,ns))
