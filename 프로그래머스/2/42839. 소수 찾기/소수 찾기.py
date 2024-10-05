def isPrime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2): 
        if number % i == 0:
            return False
    return True

from itertools import permutations

def solution(numbers):
    combined = set()
    answer = 0
    
    for length in range(1, len(numbers) + 1):
        for combo in permutations(numbers, length):
            number = int(''.join(combo))
            combined.add(number)
    
    for number in combined:
        if isPrime(number):
            answer += 1
            
    return answer