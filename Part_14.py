this_dict = {
    "brand": "Subaru",
    "model": "Outback",
    "year": 2023
}
print(type(this_dict))

friends_dict = {'name': ['Samuel', 'Galust', 'Eduard', 'Vanik', 'Tiko', 'Hakob'],
                'birthday': ['2007', '2008', '2008', '2008', '2008', '2007']}
personal_info = {'name': 'Samuel', 'Surname': 'Hovsepyan', 'birthday': 2007, 'cellphone': +37455307763}

print("--------------- List -----------------")


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


print(number_to_digit_list(2098))

print(" New list")


def divider_number_list(num):
    div_list = []
    for i in range(1, num):
        if num % i == 0:
            div_list.append(i)
    return div_list


print(divider_number_list(390))
