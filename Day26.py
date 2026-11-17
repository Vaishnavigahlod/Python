#ENCAPSULATION :
'''
#1)Private attribute example.

class Account:
    def __init__(self,actno,balance):
        self.actno=actno#public attribute
        self.__balance=balance#private attribute
        
a=Account(111,1000)
print(a.actno)
#print(a.balance)error
print(a._Account__balance)#accessing private attribute using name mangling

#2)private attribute and private method

class Account:
    def __init__(self,actno,balance):
        self.actno=actno#public attribute
        self.__balance=balance#private attribute
    #private method
    def __showbalance(self):
        print(f"balance is {self.__balance}")
        
a=Account(111,1000)
print(a.actno)
#print(a.balance)error
print(a._Account__balance)#accessing private attribute using name mangling
a._Account__showbalance()
'''
#3)private attribute and public method
class Account:
    def __init__(self,actno,balance):
        self.actno=actno#public attribute
        self.__balance=balance#private attribute
    #public method
    def showbalance(self):
        print(f"balance is {self.__balance}")
        
a=Account(111,1000)
print(a.actno)
a.showbalance()

#4)protected attribute and public method

class Account:
    def __init__(self,actno,balance):
        self.actno=actno#public attribute
        self.__balance=balance#protected attribute
class Saving(Account):
    def showbalance(self):
        print(f"balance is {self.__balance}")
        
a=Account(111,1000)
print(a.actno)
a.showbalance()




