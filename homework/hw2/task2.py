def prime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

numbers = int(input())
number_list = []
for i in range(numbers):
    number_list.append(int(input()))
for i in number_list:
    print (prime(i))
