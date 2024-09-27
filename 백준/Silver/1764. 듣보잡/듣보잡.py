N, M = map(int, input().split())

not_heard = set()
not_seen = set()

for _ in range(N):
    not_heard.add(input())

for _ in range(M):
    not_seen.add(input())

not_seen_heard = not_heard & not_seen
print(len(not_seen_heard))
for person in sorted(not_seen_heard):
    print(person)