def sum(x, y):
    if type(x) != int or type(y) != int:
        raise TypeError("One or both of args is not int")
    if x <= 0 or y <= 0:
        raise ValueError('One or both of args < 0')
    else:
        return x + y
