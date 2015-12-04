def gcd(first, second):
    if first % second == 0:
        return second
    else:
        return gcd(second, first % second)


def array_shift(array,shift):
    for i in range (gcd(len(array),shift)):
        temp = array[i]
        j = i
    while k == j + shift:
      if k >= n:
          k -= n
      elif k == i:
          break
      x[j] = x[k]
      j = k
      x[j] = t
    return array

print (array_shift([1,2,3,4,5], 5))