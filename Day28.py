'''
#ex:try , except else and finally

n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
try:
    result=n1/n2
    print(f"result is {result}")
except ZeroDivisionError as e:
    print(e)
else:
    prin("else block will execute if error does not come")
finally:  #error aaya to bhi execute hota hai
    print("finally block execute whether error occurs or not")
print("bye")

#example:division by zero error and value error
try:
    n1=int(input("Enter number 1"))
    n2=int(input("Enter number 2"))
    
    result=n1/n2
    print(f"result is {result}")
except ZeroDivisionError as e:
    print("cannot divide by zero")
except ValueError as e:
    print("please enter integer number")
else:
    print("else block will execute if error does not come")
finally:  #error aaya to bhi execute hota hai(always execute)
    print("finally block execute whether error occurs or not")
print("bye")


#INDEX ERROR :for tuple and list
fruits =["apple","banana","cherry"]
try:
    print(fruits[0])
    print(fruits[3])
except IndexError as e:
    print(f"error : {e}")
print("bye")

#KEY ERROR :for dictionary
student ={"name":"john","age":20}
try:
    print(student["name"])
    print(student["age1"])
except KeyError as e:
    print(f"key not fount in dictionary :{e}")
else:
    print("buy")
   
#GENERIC EXCEPTION (Saare types ke error le lenga)
try:
    result=10 /int(input("enter a number:"))
    print("result:",result)
except Exception as e:
    print(f"an unexpected error occurred: {e}")
    
       
#RAISE CUSTOM EXCEPTION :it raising exception if age is less then18
    #khud se exception lagana hai toh ye use karte hai.
try:
    age=int(input("enter your age:"))#raise exception if age is less than 18
    if age <18:
        raise ValueError("age should be greater than 17")
    print(f"age is {age} years old.")
except ValueError as e:
    print(f"error:{e}")
else:
    print("bye")
    
#NEGATIVE NUMBER ERROR
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number:"))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print("you entered:",num)
except NegativeNumberError as nne:
    print("Error:",nne)
except ValueError:
    print("please enter a valid number!")
 '''   
#example of raise

try:
    cust_name=input("Enter your name:")
    amount=float(input("Enter bill amount:")) #value error iss liye kyu ki float diya hai toh koi no ana cahiye
    if amount<0:
        raise Exception("amount cannot be less than zero")
     
except ValueError as e:
    print(f"error :{e}")
    
except Exception as e:
     print(f"error :{e}")
     amount=float(input("enter bill amount"))
else: # will execute if exception does not occurs
     print("else block")
finally:
     print("-------details-------")
     print(f"customer name : {cust_name}")
     print(f"bill amount : {amount}")
     print("-------thank you for purchase-------")
     

    
 
    

