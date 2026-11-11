'''
#OOPS :oop is programming paradigm (pattern) based on the concept of "objects," which combine data(attributes)
# and behaviours(methods) to model real-world entities.

#Create a class book
class Book:
      title=None
      author=None
      price=0
b=Book()
print("Enter book details:")
b.title=input("Enter title:")
b.author=input("Enter author:")
b.price=int(input("Enter price:"))
print("book details")
print(f"title :{b.title}")
print(f"author :{b.author}")
print(f"price :{b.price}")

#create a class customer having attribute cust_id, cust_name, cust_email, cust_mobile.
#create a class patient having attribute , opat_id, name, disease, doctorname

#TYPE OF ATTRIBUTE

#1)class attribute: global jo sab me share hongi,sab me common, shared by all object of the class

class student:
      comapny_name="itpreneur"
      company_mobile=95789076
      
s1=student()
s2=student()
print("s1 details")
print(s1.company_name,s1.comapny_mobile)
print("s2 details")
print(s2.company_name,s2.comapny_mobile)
print("student details")
print(student.company_name , student.comapny_mobile)

#2)instance attribute

#EX: example of instance attribute

class Customer:
   def __init__(self):
       name=""
       mobile=0
       
c1=Customer()
c1.name="vaishnavi"
c1.mobile=123

print(c1.name)
print(c1.mobile)

#example of instance attribute

class Customer:
     shopcode=111 #class attribute
     
c1=Customer()
c1.name="ram"
c1.mobile=1234
print(c1.shopcode)
print(c1.name)
print(c1.mobile)

#example of constructor with parameters

class Customer:
    def __init__(self,name,mobile):
         self.name=name
         self.mobile=mobile
         
name=input("enter name:")
mobile=int(input("enter mobile number:"))
c1=Customer(name,mobile)
print(f"name :{c1.name}")
print(f"mobile :{c1.mobile}")

#Example of constructor with parameters and method

class Customer:
   def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
  #method
   def display(self):
      print(f"name :{name}")
      print(f"mobile :{mobile}")
      
name=input("enter name:")
mobile=int(input("enter mobile number:"))
c1=Customer(name,mobile)
c1.display()

#Class attribute (shared by all instances)

class Phone:
   device_type="Smartphone"
   def __init__(self,brand,model,price):
       self.brand=brand
       self.model=model
       self.price=price
   def display(self):
       print("phone details:")
       print(f"device type :{self.device_type}")
       print(f"brand type :{self.brand}")
       print(f"model :{self.model}")
       print(f"price :{self.price}")
   def updateprice(self,price):
         self.price=price
         print("price updated")
         self.display()
         
p1=Phone("oppo","A56",15000)
p1.display()
p1.updateprice(20000)
'''
#create a class saving

class Saving:
     
     def __init__(self,actno,bal):  #constructor
         self.actno=actno  #instance attribute
         self.bal=bal      #instance attribute
     def deposit(self,amount):
         self.bal=self.bal+amount
         print("amount deposited successfully")
     def show_balance(self):
         return f"balance is {self.bal}"
a=int(input("enter account number:"))
b=int(input("enter balance:"))
s=Saving(a,b)  #object
amt=int(input("enter amount to be deposited:"))
s.deposit(amt)
print(s.show_balance())

# single inheritance: *one base class has only single child class is called as single inheritance*


