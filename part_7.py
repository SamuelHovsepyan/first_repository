def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
number = myfunc(4)

print(mydoubler(11))
print(mytripler(11))
print(number(11))

print("-------------- NEW --------------")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equale")
else:
    print("a is greateer than b")

print("_________________ NEW ________________")

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
