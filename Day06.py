'''
#************************************match is like switch*******************************************************

#eacceptday number and print dayname using match statement

dayno=int(input("enter dayno(1-7)"))
match dayno:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednusday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("default")
        
 
#accept month number and print month using match statement

month=int(input("enter month(1-12)"))
match month:
    case 1:
        print("january")
    case 2:
        print("fabruary")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("august")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
        print("december")
    case _:
        print("enter month from 1 to 12")
        
  


#accept character and print vowel or not
       
ch=input("enter character")
match ch:
    case 'a'|'e'|'i'|'o'|'u':
        print("vowel")
    case _:
        print("not a vowel")
        
 
#accept 2 number and operator and print result using match
       
n1=int(input("enter number 1"))
n2=int(input("enter number 2"))
op=input("enter operator")
match op:
    case '+':
        result=n1+n2
    case '-':
        result=n1-n2
    case '*':
        result=n1*n2
    case '/':
        result=n1/n2
    case '%':
        result=n1%n2
    case _:
        print("not a valid operator")
print(f"result: {result}")
 
#accept score and print grade

score=int(input("enter score"))
match score :
    case s if s>=90 and s<=100:
        print("grade A")
    case s if  s>=80:
        print("grade B")
    case s if s>=70:
        print("grade C")
    case s if s>=60:
        print("grade D")
    case _:
        print("fail")
        

    
#acept traffic color light and print either go, stop, ready

color=input("enter trafic light color")
match color:
    case "green":
        print("you can go")
    case "red":
        print("please stop")
    case "yellow":
        print("ready to go")
    case _:
        print("invalid color")
        
#program to accept age and print whether old, young or child
        
age=int(input("enter age:"))
        
match age:
    case a if a>=60:
        print("old")
    case a if a>=13 and a<=59:
        print("young")
    case a if a>=0 and a<=12:
        print("child")
    case _:
        print("invalid")
        
        
#accept sales_amount and print whether eligible to get discont or not(sales kam ho rhi hai toh disscount badhana honga taki customers jyada aaye)
        
sales=int(input("enter current sales:"))
match sales:
    case a if sales<=10:
        print("40% didcount")
    case a if sales<=30:
        print("25% discount")
    case a if sales<=100:
        print("10% discount")
    case _:
        print("no discount")
        
'''
