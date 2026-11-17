'''
#EXCEPTION HANDLING :error which comes at runtime is called exception.
                 #error and exception handling in python is managed using try,except,else,finally,and raise statement

#topic 1: try and except
n1=10
n2=0 #n2 0 hai or hum n1 /n2 karenge toh error ayga iss liye try or except use kiya
result=0
try :
    result=n1/n2 #error will come if n2 is zero it will caught by except block
    print(res)
except ZeroDivisionError as e:
    print(f"error : {e}")
print(f"result : {result}")
print("bye")

#ex: handle division by zero
try:
    num1 =int(input("Enter numerator: "))
    num2 =int(input("Enter denominator: "))
    result = num1/num2
    print(f"Result : {result}")
except ZeroDivisionError as e:
       print("Error: cannot divide by zero!")
print("bye")

#ex:
try:
    age=int(input("Enter your age:"))
    print(f"you are {age} years old.")
except ValueError as e:
    print(e)
print("bye")

#ex:accept bill details
try:
    cust_name=input("Enter your name:")
    amount=float(input("Enter bill amount:")) #value error iss liye kyu ki float diya hai toh koi no ana cahiye
                                              #character aa gya toh value error denga  #this block execute is acception is occurs 
except ValueError as e:
    print(f"error :{e}")
    amount=float(input("Enter bill amount:"))
    
print("-------details-------")
print(f"customer name : {cust_name}")
print(f"bill amount : {amount}")
print("---thank you for purchasing---")


#ex: try except or else

try:
    cust_name=input("Enter your name:")
    amount=float(input("Enter bill amount:")) #value error iss liye kyu ki float diya hai toh koi no ana cahiye
                                              #character aa gya toh value error denga  #this block execute is acception is occurs 
except ValueError as e:
    print(f"error :{e}")
    amount=float(input("Enter bill amount:"))
except Exception as e:
     print(f"error :{e}")
     
else: # will execute if exception does not occurs
     print("-------details-------")
     print(f"customer name : {cust_name}")
     print(f"bill amount : {amount}")
print("---thank you for purchasing---")

#example of finally

try:
    cust_name=input("Enter your name:")
    amount=float(input("Enter bill amount:")) #value error iss liye kyu ki float diya hai toh koi no ana cahiye
                                              #character aa gya toh value error denga  #this block execute is acception is occurs 
except ValueError as e:
    print(f"error :{e}")
    amount=float(input("Enter bill amount:"))
except Exception as e:
     print(f"error :{e}")
     
else: # will execute if exception does not occurs
     print("-------details-------")
     print(f"customer name : {cust_name}")
     print(f"bill amount : {amount}")
     
finally:
    print("---thank you for purchasing---")

'''
#ex: problem of string and float
    
try:
    cust_name=input("Enter your name:")
    amount=float(input("Enter bill amount:")) #value error iss liye kyu ki float diya hai toh koi no ana cahiye
    discount="20"#str
    amount=amount-discount#character aa gya toh value error denga  #this block execute is acception is occurs 
except ValueError as e:
    print(f"error :{e}")
    
except Exception as e:
     print(f"error :{e}")
     amount=amount-float(discount)
else: # will execute if exception does not occurs
     peinr("else block")
finally:
     print("-------details-------")
     print(f"customer name : {cust_name}")
     print(f"bill amount : {amount}")
     print("-------thank you for purchase-------")
     

    





    



    