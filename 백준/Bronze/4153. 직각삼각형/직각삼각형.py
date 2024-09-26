def is_right(a, b, c):
    return a**2 + b**2 == c**2

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if is_right(a, b, c) or is_right(b, c, a) or is_right(c, a, b):
        print("right")
    else:
        print("wrong")
