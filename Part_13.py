def count_of_divider(number):
    count_div = 0
    for i in range(1, number):
        if number % i == 0:
            count_div += 1
    return count_div


print(count_of_divider(10))

print("-------------- NEW ----------------")


def divider_list(num):
    div_list = []
    for i in range(1, num):
        if num % i == 0:
            div_list.append(i)
    return div_list


print(divider_list(10))

print("---------------- new ---------------")


def sum_of_divider(number):
    sum_divider = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divider += i
    return sum_divider


print(sum_of_divider(10))

print("----------------- New --------------")


def perfect_number_list(num):
    perfect_list = []
    for i in range(1, num):
        if sum_of_divider(i) == i:
            perfect_list.append(i)
    return perfect_list


print(perfect_number_list(30))

print("=================")


def is_perfect(num):
    div_sum = 0
    for i in range(1, num):
        if num % i == 0:
            div_sum += i
    return div_sum == num


print(is_perfect(6))
