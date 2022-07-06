def max_marks(a):
    i=1
    while i<len(a):
        if a[0]<a[i]:
            a[0]=a[i]
        i=i+1
    return a[0]
# list=[2,3,4,5,6,7]
# print(max_marks(list))
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
j=0
while j<len(marks):
    print(max_marks(marks[j]))
    j=j+1