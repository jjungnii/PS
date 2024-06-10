n = int(input())
sanggeun = list(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

num_sanggeun = {}
for card in sanggeun:
    if card in num_sanggeun:
        num_sanggeun[card] += 1
    else:
        num_sanggeun[card] = 1

for card in test:
    if card in num_sanggeun:
        print(num_sanggeun.get(card), end=" ")
    else:
        print(0, end=" ")