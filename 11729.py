<<<<<<< HEAD


def hanoi(N,start, end, other): 
    if N == 1: 
        print(start, end)
        return
    hanoi(N-1,start,other,end) 
    print(start,end)
    hanoi(N-1,other,end,start)

N = int(input())
print((2**N)-1)
hanoi(N, 1,3,2)

=======


def hanoi(N,start, end, other): 
    if N == 1: 
        print(start, end)
        return
    hanoi(N-1,start,other,end) 
    print(start,end)
    hanoi(N-1,other,end,start)

N = int(input())
print((2**N)-1)
hanoi(N, 1,3,2)

>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
