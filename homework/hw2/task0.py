name = str(input())
number = int(input())
if name == "утюг":  # этот if задает соответствие м/у словом и его формами
    list_of_names = ["утюг", "утюга", "утюгов"]
elif name == "ложка":
    list_of_names = ["ложка", "ложки", "ложек"]
elif name == "чайник":
    list_of_names = ["чайник", "чайника", "чайников"]
else:
    list_of_names = ["гармошка", "гармошки", "гармошек"]


def plural(number, list_of_names):
    if 20 >= number % 100 >= 5 or number % 10 == 0:
        k = 2
    elif number % 10 == 1 and number % 100 != 11:
        k = 0
    elif 4 >= number % 10 >= 2:
        k = 1
    else:
        k = 2

    word = (str(number), list_of_names[k])
    return (' '.join(word))  # выдает строку 3 ложки, например

print (plural(number, list_of_names))

