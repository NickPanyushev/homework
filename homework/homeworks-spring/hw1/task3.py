size = int(input()) #размер стека
funs_in_stack = input().split() # имена функций в стеке
line_number = int(input()) # количество строк behaviour
behaviour = dict.fromkeys(funs_in_stack) # поведение функций относительно исключений
for i in range (line_number):
    fun, catch_ex, throw_ex = input().split()
    behaviour[fun] = [inex, outex]
    if