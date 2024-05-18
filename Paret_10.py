def number_to_digit_list(number):
    digit_list = []
    temp = number
    while True:
        digit_list.append(temp % 10)
        temp = temp // 10
        if temp < 10:
            digit_list.append(temp)
            break
    digit_list.reverse()
    return digit_list


print(number_to_digit_list(5275664756))


def number_to_digit_list(number):
    digit_list = []
    temp = number
    while True:
        digit_list.append(temp % 10)
        temp = temp // 10
        if temp < 10:
            digit_list.append(temp)
            break
    digit_list.reverse()
    return digit_list
