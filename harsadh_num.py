a=int(input("enter starting point"))
b=int(input("enter ending point"))
while a<=b:
    abc=list(str(a))
    print(abc)
    i=0
    d=0
    while i<len(abc):
        d=d+int(abc[i])
        i=i+1
    if a%d==0:
        # print(a,"Harsadh number")
        print(bool(a))
    else:
        print(a)
    a=a+1