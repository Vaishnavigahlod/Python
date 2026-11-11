'''
#INHERITANCE

#single inheritance: one base class has only single child class.

#EX: of single inheritance, create a class using attribute person name,address,id,salary
class Person:  #base class
     name="vaishnavi"
     address="nagpur"
     
class Employee(Person):  #child class
    empid=123
    salary=30000
    
e1=Employee()
print(e1.name)
print(e1.address)
print(e1.empid)
print(e1.salary)
'''
#create a class using methods person name, address, id, salary
class Person:
    def getpersondata(self,name,address):
        self.name=name
        self.address=address
    def displaypersondata(self):
        print(self.name)
        print(self.address)
class Employee(Person):
    def getemployeedata(self,empid,salary):
        self.empid=empid
        self.salary=salary
    def displayemployeedata(self):
        print(self.empid)
        print(self.salary)
        
e1=Employee()
e1.getpersondata("vaishnavi","shantinagar nagpur")
e1.getemployeedata(123,70000)
e1.displaypersondata()
e1.displayemployeedata()

#Algorithm: step to solve problem
