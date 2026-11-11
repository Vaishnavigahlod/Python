#Method Overriding
class Account:
    def deposit(self):
        print("deposit method of account class")
class Saving(Account):
    #overriding th base class deposit ,ethod
    def deposit(self):
        print("deposit method of saving class")
        
s=Saving()
s.deposit()

#
class Account:
    bal=1000
    def deposit(self,amount):
        print("deposit method of account class")
class Saving(Account):
    #overriding th base class deposit ,ethod
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount+self.interest
        print(f"amount deposited , bal is {self.bal}")
        
        
s=Saving()
s.deposit(200)

#
class Account:
    bal=1000
    def deposit(self,amount):
        print("deposit method of account class")
class Saving(Account):
    #overriding th base class deposit ,ethod
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount+self.interest
        print(f"amount deposited , bal is {self.bal}")
class Current(Account):
    def deposit(self, amount):
        self.bal=self.bal+amount
        print(f"amount deposited without interest, bal is {self.bal}")        
s=Saving()
s.deposit(200)
c=Current()
c.deposit(200)

#EXAMPLE OF METHOD OVERRIDING

#constructor with supper 
class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f"name : {self.name}"
class Student(Person):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rno=rno
    def display(self):
        print(super().display())
        return f"no : {self.rno}"
    
class Parttime_student(Student):
    def __init__(self,name,rno,course):
        super().__init__(name,rno)
        self.course=course
    def display(self):
        print(super().display()) 
        return f"course: {self.course}"
    
s=Student("vaishnavi", 303)
print(s.display())

pt=Parttime_student("Ram",123,"Python") #object
print(pt.display())

        



