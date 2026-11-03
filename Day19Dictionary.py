'''
#DICTIONARIES

student={}
print(type(student))

#Ex)using KEY AND VALUE FORMATE**************

#Ex)create a dictionary to store name, age and city

          #key    #value     key vale key     vale
student={"name":"vaishnavi","age":20,"city":"nagpur"}
print(student)

#Ex)create a dictionary to store name, age and city. take input from user

n=input("Enter name:")
a=int(input("Enter age:"))
c=input("Enter city:")

student={"name":n,"age":a,"city":c}
print(student)

#Ex)using CONSTRUCTOR ***********

n=input("Enter name:")
a=int(input("Enter age:"))
c=input("Enter city:")

            #using constructor
student=dict(name=n,age=a,city=c)
print(student)

#Accessing from dictionary through key access using SQUARE bracket[] (KEY exist then it give key error)

n=input("Enter name:")
a=int(input("Enter age:"))
c=input("Enter city:")

student=dict(name=n,age=a,city=c)
print("student details")
print(f"name :{student['name']}")
print(f"age :{student['age']}")
print(f"city :{student['city']}")

#Acessing from dictionary through key acces using GET(it not return error it gives NONE)

n=input("Enter name:")
a=int(input("Enter age:"))
c=input("Enter city:")

student=dict(name=n,age=a,city=c)
print("student details")
print(f"name :{student.get('name')}")
print(f"age :{student.get('age')}")
print(f"city :{student.get('city')}")

#dictionary to store current user (id, name, role)

current_user={"id":123,"name" :"manisha","role":"admin"}
print(current_user)
print(f"id {current_user['id']}")
print(f"name {current_user['name']}")
print(f"role {current_user['role']}")


#dictionary to store current user (id,name, role)

current_user={"id":123,"name":"mayuri","role":{"admin","customer"}}
print(current_user)
print("current user details")
print(f"id {current_user['id']}")
print(f"name {current_user['name']}")
r=current_user['role'] #set
r1=list(r)
print(f"role 1 : {r1[0]}")
print(f"role 2 : {r1[1]}")

#METHODS OF DICTIONARIES

#1)KEYS(): Return a view of all keys

current_user={"id":123,"name":"mayuri","role":{"admin","customer"}}
print("keys", current_user.keys())

#2)VALUES(): return a view of all value

current_user={"id":123,"name":"mayuri","role":{"admin","customer"}}
print("values", current_user.values())

#3)ITEMS(): return a views of all key-value pairs as tuple

current_user={"id":123,"name":"mayuri","role":{"admin","customer"}}
print("items", current_user.items())

#4)GET(key,default): returns the value for key or default if the key is not found 

current_user={"id":123,"name":"mayuri","role":{"admin","customer"}}
print("get", current_user.get("id"))


#5)POP METHOD : it return last key value and removes it from dictionary

patient={"id":111,"name":"ravi","document":"vaishnavi"}
print(patient)
p1=patient.popitem()
print("pop item:",p1)
print("remaining",patient)

#6)UPDATE :update the key value

patient={"id":111,"name":"ravi","doctname":"vaishnavi"}
print(patient)
p1={"doctname":"mahi","mobile":7809765432}
patient.update(p1)
print(patient)


#EXAMPLE:

patient={}
#adding a new key value pair to dictionary
pid=int(input("enter patient id:"))
patient["id"]=pid
pn=input("enter patient name:")
patient["name"]=pn
#display the patients
print("patient details")
print(patient)
id=input("enter key to update")
val=input("enter value")
patient.update({id:val})
print(patient)

#7)CLEAR() :

#8)COPY :create a duplicate copy of a dictionary

tempadd={"area":"sadar","city":"nagpur"}
permadd=tempadd.copy()
print(permadd)
'''
#EX:
stud={}
for i in range(3):
    name=input("enter name:")
    math=int(input("enter math:"))
    chem=int(input("enter chem:"))
    stud[name]={"math":math,"chem":chem}
print(stud)








