def binary_search_in_slice(array, left_index, right_index, value):
    if left_index > right_index:
        return -1
    middle_index = (left_index + right_index) // 2
    if value > array[middle_index]:
        return binary_search_in_slice(array, middle_index + 1, right_index, value)
    elif value < array[middle_index]:
        return binary_search_in_slice(array, left_index, middle_index - 1, value)
    elif value == array[middle_index]:
        return middle_index

def binary_search(array, value = int(input())):
    return binary_search_in_slice(array, 0, len(array) - 1, value)

t = [1,3,4,68,84,67,7936,45,346,67]
t.sort()
print (t)
print (binary_search(t))

'''
Вычислительная сложность - O(log N), т.к. делим массив каждый раз пополам и, следовательно, скорость зависит от двоичного логарифма длины

'''
