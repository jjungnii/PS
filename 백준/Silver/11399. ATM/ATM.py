N = int(input())
times = list(map(int, input().split()))

accumulated = 0
result = 0

for time in sorted(times):
    accumulated += time
    result += accumulated

print(result)