# input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene 
# ke baad inn 3 mein se sabse bade number ko print karo
# Note: Isme aap loops ka use nahi kar sakte.
num=int(input("enter 1st number"))
num1=int(input("enter 2nd number"))
num2=int(input("enter 3rd number"))
if num>num1 and num>num2:
    print(num,"is maximum")
elif num1>num and num1>num2:
    print(num1,"is maximum")
elif num2>num and num2>num1:
    print(num2,"is maximum")
else:
    print("none")