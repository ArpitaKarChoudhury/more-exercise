# 1 se 1000 tak saare numbers print karne ka loop likho. Lekin
# Agar number 3 se divisible hai toh "nav" print karvao.
# Agar number 7 se divisible hai toh "gurukul" print karvao.
# Agar number 21 se divisible hai toh "navgurukul" print karvao.
a=int(input("enter nmber"))
i=1
while i<=a:
    if i%21==0:
        print("navgurukul")
    elif i%7==0:
        print("Gurukul")
    elif i%3==0:
        print("nav")
    else:
        print(i)
    i=i+1