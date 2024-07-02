from math import ceil

s = input()
cnt = 0

for idx in range(len(s) - 1):
    if s[idx] != s[idx + 1]: cnt += 1

print(ceil(cnt / 2))