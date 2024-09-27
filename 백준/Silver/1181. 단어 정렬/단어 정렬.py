num = int(input())
words = []

for _ in range(num):
    words.append(input())

words = set(words)
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)