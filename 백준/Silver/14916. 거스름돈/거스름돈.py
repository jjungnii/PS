import sys

n = int(sys.stdin.readline())

cnt = 0 # 거스름돈 동전 개수

while n:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1

if n < 0:
    print(-1)
else:
    print(cnt)