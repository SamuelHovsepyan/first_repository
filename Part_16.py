def beauty_8():
    beauty = 0
    beauty_listy = []
    for i in range(1, 10):
        beauty = beauty * 10 + i
        beauty_listy.append(beauty * 8 + i)
    return beauty_listy


print(beauty_8())


def beauty_9():
    beauty = 0
    beauty_list = []
    for i in range(1, 10):
        beauty = beauty * 10 + i
        beauty_list.append(beauty * 9 + i + 1)
    return beauty_list


print(beauty_9())

print("-------------- New ----------------")


def beauty_11():
    beauty = 0
    beauty_list = []
    for i in range(1, 10):
        beauty = beauty * 10 + 6
        beauty_list.append(beauty * (beauty + 1))
    return beauty_list


print(beauty_11())

print("-------------------- faktorial --------------------")


def factorial(num):
    number = 1
    for i in range(2, num + 1):
        number *= i
    return number


print(factorial(5))
