# PROGRAM TO CREATE A SIMPLE CALCULATOR(console)

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def avg(n1,n2):
    return n1 + n2 / 2

#user input
print("select an Operation:\n1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.AVERAGE\n\n")

select=int(input("Select an operation from 1,2,3,4,5:\n"))

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

#print a result
if select==1:
    print(num1,"+",num2,"=",add(num1,num2))

elif select==2:
    print(num1,"-",num2,"=",sub(num1,num2))

elif select==3:
    print(num1, "*", num2,"=",multiply(num1,num2))

elif select==4:
    print(num1 ,"/" ,num2 ,"=",divide(num1,num2))

elif select==5:
    
    print("(" ,num1, "+", num2, ")", "/", 2 , "=" ,avg(num1,num2))

else:
    print("Invalid operation!!..Please select again.")



