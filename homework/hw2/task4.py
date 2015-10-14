list_of_ints = [input().split(' ')]
for i in list_of_ints:
    i = int(list_of_ints[i])
print (list_of_ints)
def euclid(first, second):
    if first < second: first, second = second, first # меняем аргументы местами, если надо
    if first % second == 0:
        return second
    else:
        return euclid(second, first % second)



