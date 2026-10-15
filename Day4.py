#(QUESTION 1)customer segment(data analyst style)
#situation: classify customers based on total spend
#spend>=50000->premium, spend>=20000->gold, spend>=5000->silver, below 5000->bronze

totalspend=float(input("enter total spend:"))

if totalspend>=50000:
    segment="premium"
    elif totalspend>=20000:
        segment="gold"
        elif totalspend>=5000:
            segment="silver"
            else:
                segment="bronze"
                print("customer segment:",segment)
                
#(QUESTION 2)leap year checker
#situation: a year is a leap year if: div by 4 and if div by100, it must alseo be divby 400

year=int(input("enter year:"))

if year %4==0:
    print("year is leap year")
    elif year%100==0:
        print("year is not a leap year")
        elif year%400==0:
            print("year is leap year")
            else:
                print("nothing")
                
#(QUESTION 3)odd or even number
#situation: check whethera number is odd or even
                
num=int(input("enter a number:"))

if num %2==0:
    print("number is even")
    else:
        print("number is odd")
        
#(QUESTION 3)positive, negative or zero
#situation: check if number is positive, negative, zero
        
num=int(input("enter a number:"))

if num>0:
    print("number is possitive")
    elif num<0:
        print("number is negative")
        else:
            print("zero")
            
#(QUESTION 4) largest of two numbers
#situation: find the largest number between two numbers
            
a=int(input("enter first number:"))
b=int(input("enter second number:"))

if a>b:
    print(a,"is largest")
    elif b>a:
        print(b,"is largest")
        else:
            print("both are equal")
            
#(QUESTION 5)pass or fail
#situation:a student needs minimum 40 marks to pass check if the student has passsed or failed.
            
marks=float(input("enter marks:"))

if marks>=40:
    print("pass")
    else:
        print("fail")
        
#(question 6)day of week
#situation: take (1 to 7) and print the day of the week. 1=monday, 2=tuesday, ...7=sunday
        
day=int(input("enter day number between(1 to 7):"))

if day==1:
    print("monday")
    elif day==2:
        print("tuesday")
        elif day==3:
            print("wednusday")
            elif day==4:
                print("thursday")
                elif day==5:
                    print("friday")
                    elif day==6:
                        print("saturday")
                        elif day==7:
                            print("sunday")
                            else:
                                print("invalid day number")
                                
#(QUESTION 7) simple calculator(basic)
#situation: take two numbers and an operator(+,-,*,/) and perform the calculation.
                                
a=float(input("enter first number:"))
b=float(input("enter second number:"))
op=input("enter operator(+,-,*,/)")

if op=="+":
    print("result:",a+b)
elif op=="-":
    print("result:",a-b)
elif op=="*":
    print("result:",a*b)
elif op=="/":
    print("result:",a/b)
else:
print("invalid operator")
                    
                    
#(QUESTION 8) vowel or consonent
#situation: check whether a character is a vowel or consonent.

ch=input("enter a character:").lower()

if ch=='a'|ch=='e'|ch=='i'|ch=='o'|ch=='u':
    print("vowel")
elif ch.alpha(): #alpha check karta hai ki di gai chij alphabet hai ya nhi
    print("consonent")
else:
    print("not a letter")
    
#(QUESTIN 9)temperature check
#situation: check the temperature and give advice:
#below 10C->very cold
#10-20C->cold
#21-30C->pleasent
#above 30C->hot
    
temp=float(input("enter temperature in C:"))

if temp<10:
    print("very cold")
elif temp<=20:
    print("cold")
elif temp<=30:
    print("pleasent")
else:
    print("hot")
    
#(QUESTION 10) discount on shopping
#situation: a shop gives discount based on bill amount:
#bill<1000->no discount
#1000-5000->5% discount
#above 5000->10% discount
    
bill=float(input("enter bill amount:"))

if bill<1000:
    discount=0
elif bill<=5000:
    discount=bill*0.05
else:
    discount=bill*0.10
final_amount=bill-discount
print("discount:",discount)
print("final amount to pay:",final_amount)

#(QUESTION 11)driving eligibility
#situation:chek if a person can drive:
#age<18->cannot drive
#age 18-60->can drive
#age>60->can drive but with caution

age=int(input("enter your age:"))

if age<18:
    print("you cannot drive car")
elif age>=60:
    print("you can drive")
else:
    print("you can drive but with caution")
    
    
#(QUESTION 12)number divisible by 3 and 5
#situation:check if a number is divisible by both 3 and 5, only by 3, only by 5, or by neither.
    
num=int(input("enter number:"))

if num%3==0 and num%5==0:
    print("no is  divisible by both 3 and 5")
elif num%3==0:
    print("divisible by 3 only")
elif num%5==0:
    print("divisible by 5 only")
else:
    print("not divisible by 3 and 5")
    
 print("------------------------------------------------------------------------------------------------")
 
#(QUESTION 13)simple intrest rate
#situation: bank gives interset based on years:
#less then 1 year->5%
#1 to 3 years->7%
#more than 3 years->10%
    
years=float(input("enter number of years:"))

if year<1:
    rate=5
elif year<=3:
    rate=7
else:
    rate=10
print("interest rate:",rate,"%")

print("******************************************************************************************")

#(QUESTION 14) character type checker
#situation:chek whether the entered character is:
#uppercase letter
#lowercase letter
#digit
#special character

ch=input("enter a character:")

if ch.isupper():
    print("uppercase letter")
elif ch.islower():
    print("lowercase letter")
elif ch.isdigit():
    print("it is digit")
else:
    print("special character")
    
    
    
