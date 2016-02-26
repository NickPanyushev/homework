class fibonacci_sequence:
    def __init__(self, i):
        self.i = i
        self.array = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == 0:
            raise StopIteration
        elif self.array == [] or self.array == [1]:  # первое и второе число = 1
            self.array.append(1)
            self.i -= 1
            return 1
        else:  # ищем число фибоначчи
            self.i -= 1
            self.array.append(self.array[-1] + self.array[-2])
            return self.array[-1]

for i in fibonacci_sequence(5):
    print(i)
