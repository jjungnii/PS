N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def permutation(arr, length):
    results = []
    used = [False] * len(arr)

    def perm(path):
        if len(path) == length:
            results.append(path[:])
            return

        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                perm(path + [arr[i]])
                used[i] = False

    perm([])
    return results

results = permutation(nums, M)
for result in results:
    print(*result)