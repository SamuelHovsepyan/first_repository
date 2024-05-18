string = str()
my_str = "yerevan's nights"
next_str = '"yerevan" hotel'
print('"yerevan" hotel')
print("yerevan's nights")
print('"yerevan\'s" nights')
print("\"yerevan's\"nights")
print(my_str + " " + next_str)
print(len(next_str))
print(next_str[4])
print(next_str[1:4])
print(next_str[-1])
for ch in next_str:
    print(ch, end=" ")
print()
print(next_str.upper())
print(next_str.lower())
print(next_str.title())
print(next_str.capitalize())
print(next_str.swapcase())

print(next_str.isupper())
print(my_str.islower())

num_str = "1223"
number = 128
city_1 = "yerevan"
city_2 = "Ashtarak"
print("isdigit->", num_str.isdigit())
print(num_str.isnumeric())
alpha_str = "abcdef"
print(alpha_str.isalpha())
print("Distance of {1} to {2} is {0} km. {1} is biggerthen {2}.".format((number, city_1, city_2)))
