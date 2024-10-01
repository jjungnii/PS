N = int(input())
dp = [[0] * i for i in range(1, N + 1)]
dp[0][0] = int(input())

for i in range(1, N):
    nums = list(map(int, input().split()))
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + nums[j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + nums[j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + nums[j]
            
print(max(dp[N - 1]))