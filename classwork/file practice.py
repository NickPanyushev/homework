with open ("C:\\Users\\User\\Desktop\\Институт биоинформатики\\Python\\enzyme.small.txt", "r") as f:
    text = f.read()
description = text.split ("///\n")
print(len(descriptions))
