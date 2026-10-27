'''
#pass a and b tuple to function proces
def process(a,b):
    a1,a2=a #unpacing the tuple
    b1,b2=b #unpacking
    a1="abc1"
    a2="abc2"
    b1=0.1
    b2=0.2
    return (a1,a2),(b1,b2)
a=("abc","bbc")
b=(0.0,0.0)
a,b=process(a,b) #pass a and b tuple to function process
for i in a:
    print(i)
for j in b:
    print(j)
'''
'''
#LIST----------------
    
stud=[]
print(type(stud))
student=[123,"amit","amit@gmail.com",8765490876]
print(student)
print('student details')
print(f"roll number :{student[0]}")
print(f"student name :{student[1]}")
print(f"student email :{student[2]}")
print(f"student contact no :{student[3]}")

#1)similarly accept rno, name, email, and mobile from user, and store it in a list
#and the display the students details

rno=int(input("enter rno:"))
name=input("enter name:")
email=input("enter email:")
mobile=input("enter mobile number:")
student=[rno,name,email,mobile]
print(student)
print('student details')
print(f"roll number :{student[0]}")
print(f"student name :{student[1]}")
print(f"student email :{student[2]}")
print(f"student contact no :{student[3]}")

'''

#2)accept empno,name,salary and designation of employee and store it in a

empno=int(input("enter employee number:"))
name=input("enter employee name:")
salary=float(input("enter employee salary:"))
designation=input("enter employee designaion:")

employee=[empno, name, salary, designation]

print("employee detail")
print(f"employee phone number:{employee[0]}")
print(f"employee name:{employee[1]}")
print(f"employee salary:{employee[2]}")
print(f"employee designation:{employee[3]}")


