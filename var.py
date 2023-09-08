my_bar = 10
print(my_bar)

#정수
my_int = 10

#부동 소수점
my_float = 3.14

#복소수
my_complex = 3 +4j

print(my_int, my_float, my_complex)

my_bool = True
bFlag = False

print(my_bool, bFlag)

my_list = [1, 2, 'three', True]
IsElement = [3.14, "b", 'two', False]

print(my_list, IsElement)

print(*my_list)

my_list = [10, 3, 8, 9, 42, "hello"]

print(my_list.__len__())

print(my_list [0])

list_el = my_list [2]

print(list_el)

my_list[3] = 11

print(my_list)

n_add = my_list[3] + my_list[2]
print(n_add)

print(my_list[2:5])

print(my_list[:3])

print(my_list[0:3])

slice_ls = my_list[2:7]

print(slice_ls)

my_list = [10, 3, 8, 9, 42, "hello", slice_ls]

print(my_list)

my_list.insert(2, 4)

print(my_list)

print(my_list.index(3))

my_list.append(22)

print(my_list)

print(my_list.count(8))

print(my_list.pop())

print(my_list)

print(my_list)

my_list.reverse()

print(my_list)

my_list.extend(slice_ls)

print(my_list)

slice_ls.clear

print(slice_ls)

del my_list[2]

print(my_list)

my_tuple = (1, 2, 'three', True)
tpItem = (3.14, "b", 'two', False)

print(my_tuple)
print(tpItem)

print(my_tuple.__len__())

