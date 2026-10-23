#WHILE LOOP

#write a program to print no. from 1 to 5 using while loop.
i=1
while i<=5:
    print(i)
    i+=1
    
#wap to print no from 1 to 20 with the gap of 3.
i=1
while i<=20:
    print(i)
    i+=3
    
#wap to print even and odd no.
num=int(input("enter no:"))
while num>0:
    print(num)
    if num%2==0:
        print("even no")
    else:
        print("odd no")
    break

#wap to accept a number and print factorial.(nested while loop)
while True:
    num=int(input("enter number:"))
    fact=1
    while num>0:
        fact=fact*num
        num-=1
    print(f"fact: {fact}")
    ans=input("do you want to continue, press yes or no:").lower()
    if ans=="no":
        break
print("bye")

#password

password=input("enter password:")#Abc@123
isdigit=False
isspecial=False
special="!@#$%"
if len(password)>=8:
    for p in password:
        if p.isdigit():
            isdigit=True
        elif p in special:
            isspecial=True
    if isdigit==True and isspecial==True:
        print("password is valid")
    else:
        print("invalid password")
else:
    print("password should be atleast 8 character")
    
    