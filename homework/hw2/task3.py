first, second = input().split(' ')
first = int(first)
second = int(second)
if first < second:
    first, second = second, first


def euclid(first, second):
    if first % second == 0:
        return second
    else:
        return euclid(second, first % second)

print(euclid(first, second))
