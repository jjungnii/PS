N = int(input())
nums = list(map(int, input().split()))

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

result = 0
for num in nums:
    if is_prime(num):
        result += 1

print(result)