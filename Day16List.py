'''
#indexing starts from zero in list
#student detail. basic program
student=[123,"manisha","java"]
print("student details")
print(f"roll number:{student[0]}")
print(f"name:{student[1]}")
print(f"course name:{student[2]}")
print("details using for loop")
for s in student:
    print(s)
   
#slicing in list
         #0     1    2     3     4     5
month=["jan","feb","mar","apr","may","jun"]
print(month[1:4])
print(month[:4])
print(month[1:])
print(month[0:6:2])
print(month[::2])
print(month[4:1:-1])
'''
'''
#METHODS OF LIST

#1)append()   (use to add new vale)

student=["manish","ravi","dilip"]
print(student)
name=input("enter new student name:")
#add new vale in list
student.append(name)
print("after adding new name")
print(student)

#2)Extend()

names1=["amit", "ravi"]
print("list of names")
print(names1)
names2=["monali","radhika"]
names1.extend(names2)
print("list after extending")
print(names1)

#3)Insert() (insert any value in middle of the list)

names1=["amit","ravi"]
print("list of names")
n=input("enter name:")
names1.insert(1,n)
print(names1)

#4)Remove()

names1=["amit","ravi","manish"]
print("list of names")
n=input("enter name:")
names1.remove(n)
print(names1)

#5)POP (it returns value after that the value remove from list
         #0      1       2
names1=["amit","ravi","manish"]
print("list of name")
n=names1.pop(1)
print("name at index 1 is:",n)
print("names after pop method")
print(names1)

#6)Index

names1=["amit","ravi","manish"]
print("list of name")
n=names1.index("ravi")
print("index of ravi is:",n)

#7)Count

names1=["amit","ravi","manish","ravi"]
print("list of names")
n=names1.count("ravi")
print("count of ravi in list:",n)

#8)sort (in assending order)
names1=["amit","ravi","manish","ravi","amita"]
print("list of names")
n=names1.sort()
print("after sorting")
print(names1)

#
names1=["amit","ravi","manish","ravi","amita"]
print("list of names")
names1.sort(reverse=True)
print(names1)

#use key=len(value ke length ke hisab se arragngement)

names1=["amit","ravi","manish","ravi","amita"]
print("list of names")
names1.sort(key=len)
print(names1)

#9)Reverse()

names1=["amit","ravi","manish","ravi","amita"]
print("list of names")
names1.reverse()
print(names1)

#10)Clear()   (list ko empty kar deta hai)

names1=["amit","manish","ravi","amita"]
print("list of names")
names1.clear()
print(names1)

#list of student

names=[] #empty list

while (True):
   print("select a choice")
   print("1-add student name")
   print("2-exit")
   choice=int(input("enter choice number:"))
   
   if choice==1:
       name=input("enter student name:")
       names.append(name)
       print("name added to the list")
   elif choice==2:
       break
print("list of student")
print(names)

#same as 1st
names=[] #empty list
print("select a choice")
print("1-add student name")
print("2-exit")
while (True):
   choice=int(input("enter choice number:"))
   
   if choice==1:
       n=input("enter student name:")
       names.append(n)
       
   elif choice==2:
       break
print("list of student added")
print(names)

#add student name, rollno, course in list

names=[] #empty list
print("select a choice") 
print("1-add student name")
print("2-exit")
while (True):
   choice=int(input("enter choice number:"))
   if choice==1:
       r=int(input("enter student rollnumber:"))
       n=input("enter student name:")
       c=input("enter course:")
       stud=(r,n,c) #tuple
       names.append(stud)
       
   elif choice==2:
       break
print("list of student details")
print(names)
for i in names:
    print(i)
 '''
