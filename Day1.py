#program to declare variable to store rno, name, fees
rno=123
name="amit"
fees=1234.45
is_active=True

print("---students data is---")
print("roll no",rno)
print("name",name)
print("fees",fees)
print("is active",is_active)

#type function is used to chek datatype
print(type(rno))
print(type(name))


#input function is used to accept input from the user , by default input function str

rno=int(input("enter roll number:"))
name=input("enter name:")
fees=float(input("enter fees amount"))
is_active=bool(input("enter true or false of is active"))
print("---student details---")
print("roll number",rno)
print("name",name)
print("fees",fees)
print("is_active",is_active)




