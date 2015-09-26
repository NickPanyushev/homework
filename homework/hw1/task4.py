m = {}
s = input()
for i in range(ord('a'), ord('z') + 1):
    m[chr(i)] = 0
for letter in s:
    m[letter] += 1
s = [(letter, times) for (letter, times) in m.items() if times != 0]
s.sort()
for letter, times in s:
    print(letter, times)
