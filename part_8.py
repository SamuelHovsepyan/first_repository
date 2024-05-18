i = 1
while i < 101:
    print(i)
    i += 1
else:
    print("i is on longer less than 101")

print("---------- NEW --------------")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "cherry":
        continue
    print(x)

print("------------- new ------------")


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("______________ New _______________")


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(99))

print("_______________ YES _______________")


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Samuel", 36)
p1.myfunc()

print("--------------- papka -----------------")

num_1 = 24
num_2 = 8

print("---------------- +, -, *, %, / ----------------")

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 % num_2)
print(num_1 / num_2)

print("----------- >, >=, <, <=, ==, != --------------")

print(num_1 > num_2)
print(num_1 >= num_2)
print(num_1 < num_2)
print(num_1 <= num_2)
print(num_1 == num_2)
print(num_1 != num_2)

print("------------- and, or, not --------------")

print(num_1 > num_2 and num_1 != num_2)
print(num_1 > num_2 or num_1 == num_2)
print(num_1 > num_2 and num_1 == num_2)
print(num_1 < num_2 or num_1 == num_2)
print(True or False)
print(0 or True)

print("==============================")

number = 40
factorial = 1
for i in range(1, number + 1):
    factorial *= i

print(factorial)

print("77777777777777777777777777777")

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
