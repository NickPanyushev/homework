def selection_sort (a):
    b = [None for i in range (len(a))]
    for i in range(len(a)):
        b[i] = min(a)
        a.remove(min(a))
        print (b)
    return b

a = [12, 35, 2353, 68, 2, 6, 7]
print (a)
print (selection_sort(a))
