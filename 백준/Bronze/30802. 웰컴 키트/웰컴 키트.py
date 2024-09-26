N = int(input())
ordered = list(map(int, input().split()))
T, P = map(int, input().split())

total = 0
for ppl in ordered:
    if ppl % T == 0:
        total += (ppl // T)
    else:
        total += (ppl // T + 1)

print(total)
print(N // P, N % P)