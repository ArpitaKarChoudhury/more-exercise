students=int(input("enter number"))
amount=int(input("invest per head"))
monthly_invest=students*amount
if monthly_invest<=5000:
    print("hum bedget ke andar hein")
else:
    print("hum bedget ke bahar hein")