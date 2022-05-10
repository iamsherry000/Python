#practice 2.3 ~ 2.5 combine.
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
list3 = list1+list2

list1_set = set(list1)
list2_set = set(list2)
list3_set = set(list3)

ANS1 = list(list1_set.intersection(list2_set))
print("交集:",ANS1)

ANS2 = list(list1_set.union(list2_set))
print("聯集:",ANS2)

x = [i for i in list3 if i not in list2]
y = [i for i in list3 if i not in list1]
z = x+y
print("互斥集:",z)
