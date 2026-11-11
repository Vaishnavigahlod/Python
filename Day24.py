#ABSTACT CLASS AND METHOD

from abc import ABC,abstractmethod
#creating an abstract class for that you have inherit your class from ABC class
class Account(ABC): #abstract class
    #creating an abstract method
    bal=1000
    @abstractmethod
    def deposit(self,amount):
        pass
    
class Saving(Account):
    def deposit(self,amount):
        self.bal=self.bal+amount+500
        print("bal with interest ",self.bal)
        
class Current(Account):
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("bal without interest is ",self.bal)
        
s=Saving()
s.deposit(100)
c=Current()
c.deposit(200)
