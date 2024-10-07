def solution(brown, yellow):
    mn = brown + yellow
    for i in range(3, mn):
        if mn % i == 0:
            n = i
            m = mn // i
            if brown == 2 * m + 2 * n - 4:
                return [m, n]