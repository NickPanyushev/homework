sum1 = (lambda x, y: x + y)
#print(sum1)
#print ((lambda x, y: x + y)(1,2))
# numbers = input().split(" ")
# numbers = map(int, numbers)
# print (next(numbers))

class Map: #c помощью итератора
    def __init__(self, f, iterable):
        self.f = f
        self.it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.f(self.it))

def my_map(f, iterable):
    for element in iterable:
        yield f(element)

x = my_map(int, ["12", "13", "14"])
print(next(x))
print(next(x))
print(next(x))
print(next(x))

