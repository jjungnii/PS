N, M = map(int, input().split())
nums = list(map(int, input().split()))

S = [0]
total = 0

# 누적 합 미리 구하기
for num in nums:
    total += num
    S.append(total)

for _ in range(M):
    i, j = map(int, input().split())
    print(S[j] - S[i - 1])