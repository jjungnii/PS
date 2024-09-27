T = int(input())

for _ in range(T):
    ps = input()
    left = 0
    for p in ps:
        if left < 0:
            break
        if p == '(':
            left += 1
        else:
            left -= 1

    if left != 0:
        print("NO")
    else:
        print("YES")