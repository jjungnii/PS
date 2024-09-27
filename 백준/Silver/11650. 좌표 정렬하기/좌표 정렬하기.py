N = int(input())
positions = []

for _ in range(N):
    x, y = map(int, input().split())
    positions.append((x, y))

sorted_positions = sorted(positions, key=lambda x: (x[0], x[1]))

for position in sorted_positions:
    print(position[0], position[1])