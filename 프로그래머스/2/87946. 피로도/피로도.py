from itertools import permutations

def solution(k, dungeons):
    answer = []
    for order in permutations(dungeons):
        num, hp = 0, k
        for required, reduced in order:
            if hp >= required:
                hp -= reduced
                num += 1
        answer.append(num)
    
    return max(answer)