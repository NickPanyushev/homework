string1 = input() .split()
string2 = [int(x) for x in string1]
even = list()
odd = list()
for i in range(0, len(string2)):
    if i % 2 != 0:
        even += [spisok[i]]
        list.sort(even)
        list.reverse(even)
    else:
        odd += [string2[i]]
        list.sort(odd)
# print (even)
# print (odd)
n = 0
k = 0
result = list()
for a in range(0, len(string2)):
    if a % 2 != 0:
        result += [even[n]]
        n += 1
    else:
        result += [odd[k]]
        k += 1
print (" ".join(str(s) for s in result))
