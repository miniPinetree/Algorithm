import sys
from collections import deque
r = sys.stdin.readline

n = int(r())
card_num = deque(i for i in range(1, n+1))

while len(card_num) != 1:
    card_num.popleft()
    card_num.append(card_num.popleft())
print(card_num[0])