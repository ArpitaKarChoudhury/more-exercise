list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
while i<len(list2):
    if list2[i] not in list1:
        list1.append(list2[i])
    i=i+1
print(list1)