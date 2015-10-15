def euclid(first, second):
    if first % second == 0:
        return second
    else:
        return euclid(second, first % second)


def rpfilter(x, args):
    list_primes = []
    for i in range(len(args)):
        if euclid(x, args[i]) == 1:
            list_primes.append(args[i])
    if list_primes == []:
        return None
    else:
        return list_primes

list_of_ints = input().split(' ')
list_of_ints = [int(s) for s in list_of_ints]


x = (rpfilter(list_of_ints[0], list_of_ints))
if x is not None:
    print (' '.join(str(x[v]) for v in range(len(x))))
else:
    print (None)

