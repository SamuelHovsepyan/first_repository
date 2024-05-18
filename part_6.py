def is_prime(number):
    if number < 2: return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(is_prime(1))


def number_to_digit_list(number):
    test_num = number
    result_list = []
    while True:
        result_list.append(test_num % 10)
        test_num = test_num // 10
        if test_num < 10:
            result_list.append(test_num)
            break
    result_list.reverse()
    return result_list


print(number_to_digit_list(165437))


def digit_list_to_number(digit_list):
    result = 0
    digit_list.reverse()
    for iten in digit_list:
        result += iten * 10 ** digit_list.index(iten)
    return result


print(digit_list_to_number([2, 4, 6, 5]))


def number_to_cycle(number):
    temp = number_to_digit_list(number)
    result_list = []
    for _ in range(len(temp) - 1):
        temp.append(temp.pop(0))
        result_list.append(digit_list_to_number(temp))
    return result_list


print(number_to_cycle(164))


def number_to_cycle_list(start, end):
    result_list = []
    for i in range(start, end):
        if is_prime(i):
            pass
