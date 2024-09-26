def is_palindrome(num):
    length = len(num)
    mid = len(num) // 2 - 1
    for i in range(mid + 1):
        if num[i] != num[length - i - 1]:
            return False
    return True

while True:
    num = input()
    if num == '0':
        break
    if is_palindrome(num):
        print("yes")
    else:
        print("no")