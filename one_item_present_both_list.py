# Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list 
# banne jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. Socho aapki do list yeh hain:
from re import X


list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
i=0
list3=[]
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i] ==list2[j]:
            list3.append(list1[i])
        j=j+1
    i=i+1
print(list3)
# k=0
# while k<len(list3):
#     l=k+1
#     x=list3[k]
#     y=list3[l]
#     while l<len(list3):
#         if int(x) > int(y) :
#             z=y
#             y=x
#             x=z
#         break
#     k=k+1
# print(list3)