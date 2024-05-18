spisok = [14, 44, 24, 34]
for i in range(len(spisok)):
    spisok[i] += 2
print(spisok)

print("----------- NEW -------------")


class ParentClass:
    def method1(self):
        print("Method1 of ParentClass")

    def method2(self):
        print("Method2 of ParentClass")


class ChildClass(ParentClass):
    def method3(self):
        print("Method3 of ChildClass")


print(ParentClass)

print("-------- While loops ---------")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

print("--------- Functions ---------")


def my_function(fname):
    print(fname + "100")


my_function("6")
my_function("9")
my_function("20")

print("----------------- New das ---------------")

num_1 = int(input("input 1st number: "))
num_2 = int(input("input 2st number: "))
test_list = [1, 2, 3, 4]
try:
   # print(test_list[num_1])
    if num_2 == 1:
        raise ZeroDivisionError
    else:
        print(num_1 / num_2)
except ZeroDivisionError:
    print("division by zero")
except ArithmeticError:
    print("AritmeticError")
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")
except IndexError:
    print(test_list[-1])
    print("IndexError")
except Exception:
    print("Exception")
else:
    print("else block")
finally:
    print("finally block")
