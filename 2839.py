<<<<<<< HEAD
import sys
r = sys.stdin.readline

n = int(r())
quotient_5 = n//5 #5키로 봉지 개수 / 3의 몫 = 3키로 봉지 개수
remainder_5 = n%5

while True:
    if quotient_5 < 0:
        print(-1)
        break

    elif remainder_5%3 ==0:
        quotient_3 = remainder_5//3
        print(quotient_5+quotient_3)
        break
    else:
        quotient_5 -=1
        remainder_5 +=5

=======
import sys
r = sys.stdin.readline

n = int(r())
quotient_5 = n//5 #5키로 봉지 개수 / 3의 몫 = 3키로 봉지 개수
remainder_5 = n%5

while True:
    if quotient_5 < 0:
        print(-1)
        break

    elif remainder_5%3 ==0:
        quotient_3 = remainder_5//3
        print(quotient_5+quotient_3)
        break
    else:
        quotient_5 -=1
        remainder_5 +=5

>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
