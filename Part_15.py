my_tupl = tuple()
next_tupl = (5, 76, 89, 90, 93, 98)
print(type(next_tupl))
print(next_tupl.index(90))
print(len(next_tupl))
for i in next_tupl:
    print(i)

print("--------------- set ------------")

my_set = set()
next_set = {5, 8, 12, 17, 26, 67, 89}
print(type(next_set))
next_set.add(17)
print(next_set)
temp_set = {4, 8, 45, 26, 67, 101, -4}
print(next_set.union(temp_set))
print(next_set.intersection(temp_set))
print(next_set.difference(temp_set))
print(temp_set.difference(next_set))
next_set.intersection_update(temp_set)
print(next_set)
print(len(next_set))
print(17 not in next_set)
print(max(temp_set))
print(min(next_set))
