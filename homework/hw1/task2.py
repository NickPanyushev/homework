string = input(). split()
summa = 0
for n in range(0, len(string)):
    summa += int(string[n])
mean = summa / len(string)
print(mean)
