#function:
'''
#creat a function display to print("hello from itp")
def display():
    print("hello from itp")
    print("your current batch is dads")

print("calling the function display")
display()
print("again calling the function display")
display()

#function square with one parameter to square the number.
def square(num):
    sq=num*num
    return sq
num=int(input("Enter Number:"))
result=square(num)
print(f"square of a number is:{result}")


#function to print factorial of a number.
def factorial(num):
    fact=1
    while(num>0):
        fact=fact*num
        num-=1
    return fact
n=int(input("enter number:"))
result=factorial(n)
print(f"factorial :{result}")

#create a function calculate with 3 parameter to accept 2 no and 1 operator.
def calculate(n1,n2,op):
    result=0
    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1*n2
    else:
        print("invalid operator")
    print(f"result is :{result}")
    
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
operator=input("enter operator(+,-,*)")
calculate(num1,num2,operator)


#function to check username and password
def check(username,password):
    if username=="admin" and password=="admin123" :
        print("login successfull")
    else:
        print("invalid username or password")
        
u=input("enter username:")
p=input("enter password:")
check(u,p)
'''
#function to calculate 3 argument to accept 3 subject marks and print total
#and percentage and grade
def marks(m1,m2,m3):
    total=m1+m2+m3
    percentage=total/300*100
    print("total:",total)
    print("percentage:",percentage)
    
    if percentage>=90:
        print("grade A")
    elif percentage>=75:
        print("grade B")
    elif percentage>=60:
        print("grade C")
    else:
        print("fail")
m1=int(input("enter marks of 1st subject:"))
m2=int(input("enter marks of 2nd subject:"))
m3=int(input("enter marks of 3rd subject:"))
marks(m1,m2,m3)


#function calculate with one argument to accept unit and calculate bill_amount
#-0-100-8rs
#101-300-12rs
#>300-15rs

