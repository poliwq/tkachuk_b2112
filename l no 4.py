# import math
# from random import randint
#
# lst = []
# print(lst)
# lst.append(math.pi)
# lst.append(math.e)
# print(lst)
# lst.clear()
# print(lst)
# size = int(input())
# for i in range(10):
#     lst.append(randint(-10, 10))
# print(lst)
#
# print(lst[3])
#
# lst2 = [randint(-10, 10) for i in range(10)]
# print(lst2)
#
# lstNum = [i for i in range(10)]
# print(lstNum)
#
# lst_even = [i for i in range(10) if i % 2 == 0]
# print(lst_even)
#
# lst_odd = [i for i in range(10) if i % 2 != 0]
# print(lst_odd)
#
# lst_mult_square = [i**2 for i in range(10)]
# print(lst_mult_square)
#
# for i in lst_mult_square:
#     print(i)

from random import randint
lst = [randint(-10, 10) for i in range(20)]
print(lst)

sum_negative = 0

for num in lst:
    if num < 0: sum_negative += num
print("sum negative item list: ", sum_negative)

from random import randint
sum_elements_mult_3 = 0
for i in range(len(lst)):
    print(lst[i])
    if i % 3 == 0:
        sum_elements_mult_3 += lst[i]
print("sum elements that are multiples of 3: ", sum_elements_mult_3)

mult_range = 1
min_value_list = min(lst)
max_value_list = max(lst)
index_min = lst.index(min_value_list)
index_max = lst.index(max_value_list)
if index_max < index_min:
    index_max, index_min = index_min, index_max
for i in range (index_min, index_max, 1):
    mult_range *= lst[1]
print("elements between minimum and maximum, mult range is ")


