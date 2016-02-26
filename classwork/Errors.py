import traceback

'''def a(i):
    b(i-1)

def b(i):
    if i > 0:
        a(i - 1)
    else:
        traceback.print_stack()
a(5)

try:
    15 / 0
except ZeroDivisionError:
    print("It's ALIVE")'''

'''def f(x):
    try:
        return 15 / x
    except TypeError:
        print('Type Error=(')
    except ZeroDivisionError:
        print('WTF')
    print(f(4))'''

def f(x):
    try:
        return 15 / x
    except (TypeError, ZeroDivisionError) as err:
        print(type(err))
        print(err)
        print(err.args)
    print(f(4))

# try:
#     x = open("test.txt", "r")
# except FileNotFoundError:
#     print("Bad path")
# else:
#     data = x.read()
#     print(data)
#     x.close()
#
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print('result is', result)
#     finally:
#         print("executing finally clause")
# divide(2, 1)

def append(x,el):
    if not type(x) is list:
        raise TypeError("first arg should be list")
    else:
        x.append(el)
x = []
append(x, 4)
append(x, 6)
print(x)
append("", 5)