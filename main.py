my_list = list()
print(type(my_list))

next_list = [7, 9, True, 9, 8.9]
print(type(next_list))
print(next_list)
next_list.append(100)
print(next_list)
next_list.insert(0, 100)
print(next_list)
next_list.insert(0, 90)
print(next_list)
print(next_list.index(100, 2))
next_list.remove(100)
print(next_list)
print(next_list.pop(3))
print(next_list)