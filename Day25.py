#POLYMORPHISM
'''
#EX:polymorphism (runtime polymorphism).with inheritance(have 1 parent class shape  and two child class circle and rectangel
class Shape:
    def draw(self):
        pass
class Circle(Shape):
    def draw(self):
        print("Draw method of circle class")
class Rectangle(Shape):
    def draw(self):
        print("Draw method of rectangle class")
def call_draw(shape):
    shape.draw()
    
obj=input("Enter circle or rectangle:")
c=""
if obj=="circle":
    c=Circle()
elif obj=="rectangle":
    c=Rectangle()
call_draw(c)

#without inheritance polymorphism
class Circle():
    def draw(self):
        print("Draw method of circle class")
class Rectangle():
    def draw(self):
        print("Draw method of rectangle class")
def call_draw(s):
    s.draw()
obj=input("Enter circle or rectangle:")
c=""
if obj=="circle":
    c=Circle()
elif obj=="rectangle":
    c=Rectangle()
call_draw(c)
'''
#EX)
#create a base class account having method deposit, create child clas saving and current override the
#deposit method, create a method call_deposit to achive polymorphism.
