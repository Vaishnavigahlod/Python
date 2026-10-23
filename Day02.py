# A variable type can change
#during execution by assigning a new vale of a differnet type
num=20
print(type(num))
num=20.2
print(type(num))
num="hello"
print(type(num))

#multiple variable in one line

n1,n2,n3=10,20,30
print(f"num1 :{n1}, num2 :{n2}, num3 :{n3}")

#type converstion

n1="12"
n2="33"
result=int(n1)+int(n2)
print(f"result : {result}")


#
p1="13"
p2="14"
result=p1+p2
print(result)

#converting into boolean
#convert input to a boolean (eg, for yes/no qestions)
is_student = input("Are you a student? (yes/no):").lower()=="yes"
print("student status:", is_student) #Output: student status: True
#(if input is"yes")


#accept multiple inputs
#split input string to accept multiple values
n1,n2,n3=input("enter three numbers(seperated by space):").split(",")
print(f"n1={n1}, n2={n2}, n3={n3}")

#accept multiple inputs
#split input string to accept multiple values
n1,n2,n3=input("enter three numbers(seperated by space):").split()
print(f"n1={n1}, n2={n2}, n3={n3}")
total=int(n1)+int(n2)+int(n3)
print(f"total:{total}")



#program to accept length and breadth in same line and print area
length, breadth=input("enter two numbers(seperated by space):").split()
print(f"length={length},breadth={breadth}")
area=int(length)*int(breadth)
print(f"area:{area}")


#wap to accept radius, then print area of circle(pi*r*r)
radius=int(input("enter radius:"))
area=3.14*radius*radius

print("area of circle is ", area)
circumference=2*3.14*radius
print("circumference", circumference)

