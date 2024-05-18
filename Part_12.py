import turtle


def david(number):
    turtle.shape('turtle')


turtle.shapesize(2)
turtle.color('green', 'yellow')
turtle.speed(10)

for step in range(6):
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(50)
        turtle.left(360 / 3)
    turtle.end_fill()

    turtle.forward(50)
    turtle.right(60)

turtle.hideturtle()

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
