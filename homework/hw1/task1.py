name = input()
n = int(input())
if name == "утюг":
    if 20 >= n % 100 >= 5 or n % 10 == 0:
        print(str(n) + " утюгов")
    elif n % 10 == 1 and n % 100 != 11:
        print(str(n)+" утюг")
    elif 4 >= n % 10 >= 2: 
        print(str(n) + " утюга")
    else:
        print(str(n) + " утюгов")
elif name == "ложка":
    if 20 >= n % 100 >= 5 or n % 10 == 0:
        print(str(n) + " ложек")
    elif n % 10 == 1 and n % 100 != 11: 
        print(str(n) + " ложка")
    elif 4 >= n % 10 >= 2: 
        print(str(n) + " ложки")
    else:
        print(str(n) + " ложек")


