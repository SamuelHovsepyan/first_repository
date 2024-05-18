my_list = [11, 19, 23, 34, 45, 56, 67, 78, 89, 90, 1223, 345, 567, 789, False, 790, 799, True, 23, 34, 45, 45, 45, 45, ]
print(my_list[2])
print(my_list[2:6])
print(my_list[1:9:2])
print(my_list[-2])
print(len(my_list))
print(my_list[len(my_list) - 2])
print(my_list.index(19))
print(my_list.index(34, 6))
next_list = my_list.copy()
if my_list.count(11) > 0:
    my_list.remove(11)
    my_list.remove(19)
print(my_list)
print(next_list)
print(my_list)
my_list.sort()
print(my_list)
print(sum(my_list))
print(max(my_list))
print(min(my_list))

print("--------------- String -------------------")

my_String = {}
S1 = '22'
S2 = '78'
my_String = (S1 + S2)
print(my_String)

print("-------------------------- while -------------------------------")

i = 1
while i <= 10:
    print(i)
    i += 1

print("------------- for --------")

spisok = [10, 40, 20, 30]
for element in spisok:
    print(element + 2)

for i in range(10):
    print(i)

print("------------ dict -------")

my_dict = {
    "brand": "Mercedes",
    "model": "E-63",
    "year": 2023
}
print(my_dict)

print("---------- string --------")

S1 = '22'
S2 = '78'
my_string = S1 + S2 + "abc"
print(my_string)

string = str()
string_ = ""
string__ = ''
for i in my_string:
    print(i + "2")
print(len(my_string))

print("---------------- New --------------------")

num_1 = 11
num_2 = 21
if num_1 % 2 == 0 and num_2 % 2 == 0:
    print(int((num_1 + num_2) / 2))
elif num_1 % 2 == 1 and num_2 % 2 == 1:
    print((num_1 + num_2) / 2)
else:
    print((num_1 + num_2 + 1))
