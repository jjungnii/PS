N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]


def combination(arr, length):
    results = []

    def comb(path, start):
        if len(path) == length:
            results.append(path[:])
            return

        for i in range(start, len(arr)):
            comb(path + [arr[i]], i + 1)

    comb([], 0)
    return results


results = combination(nums, M)

for result in results:
    print(*result)