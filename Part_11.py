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


def happy_ticket():
    happy_number_list = []
    for i in range(100000, 1000000):
        temp = number_to_digit_list(i)
        if temp[0] + temp[1] + temp[2] == temp[3] + temp[4] + temp[5]:
            happy_number_list.append(i)
    return happy_number_list


print(happy_ticket())

print("-------------- NEW ------------")


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


def count_of_happy_number():
    happy_count = 0
    for i in range(100000, 1000000):
        temp = number_to_digit_list(i)
        if temp[0] + temp[1] + temp[2] == temp[3] + temp[4] + temp[5]:
            happy_count += 1
    return happy_count


print(count_of_happy_number())

print("-----------------new-----------------")

def odd_number(number):
    if number % 2 == 1 and number % 10 == 3:
        return True
    else:
        return False
print(odd_number(121))