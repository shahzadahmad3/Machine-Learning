def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a, b):
    return a*b
def division(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)

print("Select one option from the below:- \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
options=int(input("Enter Option Here:- "))


a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

if options==1:
    result=addition(a,b)
    print("The Answer is: ", result)
elif options==2:
    result=subtraction(a,b)
    print("The Answer is: ", result)
elif options==3:
    result=multiplication(a,b)
    print("The Answer is: ", result)
elif options==4:
    result=division(a,b)
    print("The Answer is: ", result)
else:
    print("Invalid option...")