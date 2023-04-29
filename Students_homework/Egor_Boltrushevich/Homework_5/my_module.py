my_variable = 35

#НОД
def my_func(x, y):

    while int(x) > 0 and int(y) > 0:
        if int(x) > int(y):
            x = int(x) % int(y)
        else:
            y = int(y) % int(x)
    return int(x + y)


