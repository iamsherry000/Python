# practice 2.3 兩個串列的交集
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
list3 = list1+list2

x = [i for i in list1 if i in list2]
print("交集=",x)

list1_set = set(list1)
list2_set = set(list2)
list3 = list(list1_set.intersection(list2_set))
print("交集:",list3)

# practice 2.4 兩個串列的聯集
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
list3 = list1+list2

list3_set = set(list3)
union = list(list3_set)
print("聯集=",union)

list1_set = set(list1)
list2_set = set(list2)
list3 = list(list1_set.union(list2_set))
print("聯集:",list3)

# practice 2.5 兩個串列的互斥集
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
list3 = list1+list2

list3_set = set(list3)
union = list(list3_set)

x = [i for i in list3 if i not in list2]
y = [i for i in list3 if i not in list1]
z = x+y
print("互斥集:",z)
