#TYPES OF FUNCTION
# positional, keyword, default, and variable-length arguments, with examples for each.
 
#1. Positional Arguments
  #These are arguments passed to a function in the order they are defined.
  #The position determines which parameter receives which value.
 
#Example: 
def add(a, b):
    return a + b
 
result = add(3, 5)  # Positional: a=3, b=5
print(result)  # Output: 8

#2. Keyword Arguments
  #These are arguments passed by explicitly specifying the parameter name,
  #allowing you to pass them in any order.
 
#Example: 
def greet(name, message):
    return f"{message}, {name}!"
 
print(greet(name="Alice", message="Hello"))  # Keyword: name="Alice", message="Hello"
print(greet(message="Hi", name="Bob"))       # Keyword: order doesn't matter
   # (Output: Hello, Alice!)
   # (Output: Hi, Bob!)
   
#function t calculate electricity bill
def cal_bill(cust_name,unit,rate):
    total=unit*rate
    print("bill details")
    print(f"customer name:{cust_name}")
    print(f"total amount:{total}")
    
cal_bill(unit=250,rate=7.5,cust_name="amit")

#function returning a value, function to calculate electricity bill 
def cal_bill(cust_name,unit,rate):
    total=unit*rate
    print("bill details")
    print(f"customer name:{cust_name}")
    return total
    
result=cal_bill(unit=250,rate=7.5,cust_name="amit")
print(f"total amount:{result}") 
 
#3. Default Arguments
    #These are parameters with default values, used if no argument is provided for them.
 
#Example:
def greet(name, message="Hello"):
    return f"{message}, {name}!"
 
print(greet("Alice"))          # Uses default message
print(greet("Bob", "Welcome")) # Overrides default
  # (Output: Hello, Alice!)
  # )Output: Welcome, Bob!)

#print contact details full name, phoneno,city
def contact(fullname,phonenumber,city="nagpur"):
    print("----contact details-----")
    print(f"full name : {fullname}")
    print(f"phone number : {phonenumber}")
    print(f"city : {city}")
  #ACCEPT DETIALS
fn=input("enter full name")
ph=input("enter phone number")
ch=input("do you want to enter city press yes or no")
if ch=="yes":
    city=input("enter city")
    contact(fn,ph,city)
else :
    contact(fn,ph)

#function to calculate electricity bill
def cal_bill(cust_name,unit,rate==5.5):
    total=unit*rate
    print("bill details")
    print(f"customer name:{cust_name}")
    return total
result=cal_bill("manish kumar",350,8.0)
print(f"total amount:{result}")

result=cal_bill("ravish kumar",350)
print(f"total amount:{result}")

    
#4. Variable-Length Arguments
    #These allow a function to accept an arbitrary number of arguments. There are two types:
 
     #(i)*args: Collects extra positional arguments into a tuple.
     #(ii)**kwargs: Collects extra keyword arguments into a dictionary.

#EX) variable length arguments, if you want to send arbitary no. of argument
def cal_sales_amount(*args):
    l=len(args)
    print("length:",l)
    total=0
    for i in range(l):
        total=total+args[i]
    print(f"total sales amount:{total}")
cal_sales_amount(120,500,350)

#function having variable length argument for fees
def cal_sales_amount(*args):
    l=len(args)
    print("length:",l)
    total=0
    for i in range(l):
        total=total+args[i]
    return total
amount1=float(input("enter amount 1:"))
amount2=float(input("enter amount 2:"))
amount3=float(input("enter amount 3:"))
target_amount=cal_fees_amount(amount1,amount2,amount3)
print(f"total fees amount paid:{target_amount}Rs.")

 