'''
#SET =>Mutable Unordered Collection With Unique Items {}
  
#stud={111,"amit","java","amit"}
  
#using set constructior

stud=set([111,"amit","java","amit"])
print(stud)

#1)UNION(|) =>combines all elements from both sets

stud1={"vaishnavi","mayuri"}
stud2={"Altamash","Yash"}
stud3={"Tanu","nikita"}
stud=stud1 | stud2 | stud3
print("all student")
print(stud)

#2)INTERSECTION(&) =>TO get common set from both sets

stud1={"amit","manish","amit"}
stud2={"ravi","amit"}
stud=stud1 & stud2
print("common element")
print(stud)

#3)difference(-) =>Returns elements from one set not other

stud1={"amit","manish","ravina","mona"} #jo neche vali list me nhi hai uss ko diference element le lenga
stud2={"ravina","amit"}
stud= stud1 - stud2
print("difference in student")
print(stud)

#ex:difference=employee attendance

days={"mon","tue","wed","thu","sat"}
attendance={"tue","thu","fri"}
absent=days - attendance
print("employee absent on:")
print(absent)

#4)SYMMETRIC DIFFERENCE(^)

month={"jan","feb","mar","apri","may"} #dono me jo same nhi hai uss ko nikalenge alag
attendance={"jan","mar","may"}
absent=month ^ attendance
print("difference:")
print(absent)

#5)SUBSET #2nd row ke name 1st row me hai ya nhi check karnge. agar 1 bhi alag hai toh false aaynge , 2same rahe toh bhi false kyu ki 1 alag hai

course1={"java","python","php","html","oracal"}
course2={"oracal","php"}
result=course2<=course1
print(result)

#6)SUPERSET

course1={"java","python","php","html","oracal"}
course2={"oracal","php"}
result=course1>=course2

#METHODS OF SET

#1)ADD METHOD

#ex:add 3 course in set

course=set()

for i in range(3):
    c=input("Enter course name:")
    course.add(c)
    print("course added to set")
print("course available")
print(course)

print(result)

#2)REMOVE METHOD

course={"java","php","html"}

c=input("Enter course name to remove:")
course.remove(c)
print("course removed from set")
print("course available")
print(course)

#3)DISCARD METHODS

course={"java","php","html"}

c=input("Enter course name to discard:")
course.discard(c)
print("course discard from set")
print("course available")
print(course)
'''
#4)POP METHOD

course={"java","php","html"}

c=course.pop()
print("course popped",c)
print("course set")
print("course avilable")
print(course)

#5)CLEAR METHOD

course={"java","php","html"}

c=course.clear()
print("course popped",c)
print("course set")
print("course avilable")
print(course)









