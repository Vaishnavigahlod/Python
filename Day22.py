#Customer has a account(Has a relationship)
'''
class Customer:
    def __init__(self,customer_id,name): #constructor
        self.customer_id=customer_id
        self.name = name
        self.accounts=[]
    def add_account(self, account):
        self.accounts.append(account)
#creating a class account
class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance
#execution of program start here
c=Customer(123,'vaishnavi')#it will call customer class constructor
a=Account(1,1000)#it will call account class constructor
c.add_account(a)
print("customer details")
print(f"customer id : {c.customer_id}")
print(f"customer name : {c.name}")

#display account details through customer object
print(f"Account No : {c.accounts[0].account_no}")
print(f"Balance : {c.accounts[0].balance}")

#student details
class Student:
        def __init__(self,roll_no,name): #constructor
            self.roll_no=roll_no
            self.name=name
            self.addresses=[]
        def add_address(self, address):
            self.addresses.append(address)
#create a class address
class Address:
        def __init__(self, locality, city, state):
            self.locality=locality
            self.city=city
            self.state=state
#execution of program stared from here
s=Student(1,'Tanu')
a=Address('pauni','Nagpur','Maharashtra')
s.add_address(a)
print("Student Details")
print(f" student roll no : {s.roll_no}")
print(f" student Name : {s.name}")

#display address details through  student object
print(f"locality : {s.addresses[0].locality}")
print(f"city : {s.addresses[0].city}")
print(f"state : {s.addresses[0].state}")


#2)HEIRARCHICAL INHERITANCE :parent class has one or more child class

#EX:
class Account:     #singhle inheritance
    def __init__(self,act_no,bal):
        self.act_no=act_no
        self.bal=bal
    def show_balance(self):
        return f"balance is {self.bal}"
class Saving(Account):
    intrest=500
    def deposit(self,amount):
        self.bal=self.bal+amount+self.intrest
        return f"amount deposited with intrest, bal is {self.bal}"
s=Saving(123,1000)
print(s.deposit(100))
print(s.show_balance())
#single combine with heirarchical inheritance
class Current(Account):
    def deposit(self,amount):
        self.bal=self.bal+amount
        return f"amount deposited without intrest, bal is {self.bal}"
s=Saving(123,1000)
print(s.deposit(100))
print(s.show_balance())

c=Current(124,1000)
print(c.deposit(500))
print(c.show_balance())

#3)multilevel inheritance :one child has two parent class

#EX:multilevel inheritance with attribute.
class Person:
    name="Ram"
class Employee(Person):
    salary=50000
class Parttime_Employee(Employee):
    no_hours=6
    
p=Parttime_Employee()
print(f"name {p.name}")
print(f"salary {p.salary}")
print(f"no of hours {p.no_hours}")

#EX)multilevel inheritance with method

class Person:
  def get_name(self,name):
    self.name=name
    return self.name
class Employee(Person):
  def get_salary(self,salary):
      self.salary=salary
      return self.salary
class Parttime_Employee(Employee):
  def get_hours(self,hours):
      self.no_hours=no_hours
      return self.no_hours
    
    
p=Parttime_Employee()
print(f"name {p.get_name('ram')}")
print(f"salary {p.get_salary(15000)}")
print(f"no of hours {p.get_hours(5)}")
class Person:
    name="Ram"
class Employee(Person):
    salary=50000
class Parttime_Employee(Employee):
    no_hours=6
    
p=Parttime_Employee()
print(f"name {p.name}")
print(f"salary {p.salary}")
print(f"no of hours {p.no_hours}")

#3)MULTIPLE INHERITANCE: MULTIPLE A CLASS INHERITE FROM MORE THEN 1 PARENT CLASS.
class Phone: #parent class
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
        
    def make_call(self, number):
        return f"{self.brand} {self.model} is calling {number}"
    
    def send_message(self, number, message):
        return f"{self.brand} {self.model} sent message to {number}: {message}"
  #parent class2:camera  
class Camera:  #parent class
    def __init__(self,resolution):
        self.resolution=resolution
        
    def take_photo(self):
            return f"taking photo with {self.resolution}MP camera"
        
    def record_video(self):
            return f"Recording video with {self.resolution}MP camera"
        
class Smartphone(Phone,Camera): #child class
    def __init__(self,brand,model,resolution):
        Phone.__init__(self,brand,model)
        Camera.__init__(self,resolution)
#creating object of smartphone
s=Smartphone("OPPO","A53","100")
print(s.make_call(12345))
print(s.send_message(123,'hello from nagpur'))
print(s.take_photo())
print(s.record_video())


#PRACTICE QUESTION OF INHERITANCE
#1)single inheritance -Person and employee
# Create a class Person with attributes name and age, and a method display() to print them.
# Create a class Employee that inherits from Person and adds an attribute salary with a method
# to display all details.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display(self):
        super().display()
        print(f"salary : {self.salary}")
e1=Employee("Ram",22,30000)
e1.display()

#2)Single inheritance-vehicle and car
#Create a class Vehicle with a method fuel_type() that prints "Uses petrol/diesel".
#Create a class Car that inherits from Vehicle, adds a method num_wheels() that prints "4 wheels",
#and calls both methods from an object of Car.
class Vehicle:
    def fuel_type(self):
        print("uses petrol/ diesel")
class Car(Vehicle):
    def num_wheels(self):
        print("4 wheels")
        
c1=Car()
c1.fuel_type()
c1.num_wheels()
 '''
#3)Heirarchical inheritance -shape,circle,rectangle
#Create a base class Shape with a method info() that prints "This is a shape".
#Create two classes Circle and Rectangle that both inherit from Shape.Add a method area() in each to calculate
#and print their respective areas (take radius/length & breadth as input).
class Shape:
    def info(self):
        print("This is shape")
class Circle(Shape):
    def area(self):
        radius=float(input("Enter radius of a circle:"))
        area=3.14*radius*radius
        print(f"Area of a circle: {area:.2f}")
class rectangle(Shape):
    def area(self):
        length=float(input("Enter length:"))
        breadth=float(input("Enter breadth:"))
        area=length*breadth
        print(f"Area of a rectangle : {area:.2f}")
c=Circle()
c.info()
c.area()

r=Rectangle()
r.info()
r.area()

    




        

    