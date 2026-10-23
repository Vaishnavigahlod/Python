#conditional statement
#accept age and print eligible to vote or not
age=int(input("enter age"))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
    
#greater of 3 number
n1=int(input("enter number 1 :"))
n2=int(input("enter number 2 :"))
n3=int(input("enter number 3 :"))
if(n1>n2 and n1>n3):
    print("n1 is greater")
elif(n2>n3):
    print("n2 is greater")
else:
    print("n3 is greater")

    
# write a program to print 3 subject marks and percentage and total, grade

m1=int(input("enter marks 1:"))
m2=int(input("enter marks 2:"))
m3=int(input("enter marks 3:"))
total=m1+m2+m3
per=(total/300)*100

if per>=90:
    grade="A grade"
elif per>=80:
    grade="B grade"
elif per>=70:
    grade="C grade"
elif per>=60:
    grade="D grade"
else:
    grade="fail"
print(f"total:{total}, percentage:{per:.2f}, grade:{grade}")


#use of .2f , .3f , etc
per=12.34577
print(format(per,".2f"))



#accept number and print positive or negative or equal to 0

num=int(input("enter number"))
if num>0:
   print("positvie")
elif num<0:
    print("negative")
else:
    print("equal to zero")
    
    
#accept username and password (username=admin, pwd=admin123)
    
username=input("enter username")
password=input("enter password")
if username=="admin":
    if password=="admin123":
        print("login succesfull")
    else:
        print("invalid password")
else:
     print("invalid username")
     
#accept bill_amount and print delivery_charge
     #(above 1000 free, between 500 and 1000-100rs, below 500 50rs)
     
bill_amount=int(input("enter bill amount"))
delivery_charge=0
if bill_amount>=1000:
    delivery_charge=0
    elif bill_amount>500:
        delivery_charge=100
        else:
            delivery_charge=50
            print("delivery charge:",delivery_charge)
            total=bill_amount+delivery_charge
            print("total amount payable:",total)
            
            
            
     
     
     
    

    
    
