def prime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

def euclid(first, second):
    if first % second == 0:
        return second
    else:
        return euclid(second, first % second)
print("I'm so awesome, I've created a module!!")

print(__name__)
if __name__ == "main":
    for i in range(2,1000):
        if prime(i):
            print(i)
        
