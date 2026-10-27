#how to pass tuple to a function
'''
def calculate(m):
    print(type(m))
    sum=0
    for i in m:
        sum+=i
    print(f"total marks",sum)
    
m1=int(input("enter marks"))
m2=int(input("enter marks"))
m3=int(input("enter marks"))
marks=(m1,m2,m3)
calculate(marks) #passing tuple function

#ex:variable length argument (*args)
def calculate(*args):
    print(type(args))
    sum=0
    for i in args:
        sum+=i
    print(f"total marks",sum)
    
m1=int(input("enter marks"))
m2=int(input("enter marks"))
m3=int(input("enter marks"))
calculate(m1,m2,m3)

#function returning a tuple
def calculate(r):
    area=3.14*r*r
    circ=2*3.14*r
    ci=(area,circ)  #tuple
    return ci

radius=int(input("enter radius"))
result=calculate(radius)
print(f"area of circle :{result[0]}")
print(f"circumferance of circle :{result [1]:.2f}")

'''

#count function in tuple
age=(18.20,18,23,24,55)
l=len(age)
print(f"length :{l}")
for i in range(l):
    print(age[i])
num=int(input("enter age"))
c=age.count(num)
print(f"count of age {num} in tuple :{c}")
ind=age.index(num)
print(f"index of {num} is : {ind}")


