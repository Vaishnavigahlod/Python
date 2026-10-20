'''
#LOOPS
#using for loop print "ITpreneur" 5 times
for i in range(5):
    print(f"ITpreneur:{i}")
print("bye")

#using for loop print numbers from 1 to 5
for i in range(1,6):
    print(f"i:{i}")
print("bye")


#using for loop print numbers from 51 to 60
for i in range(51,61):
    print(i)
print("bye")

#using for loop print odd number bretween 1 to 10

for i in range(1,11,2):
    print(f"i:{i}")
print("bye")

#wap to print even no from 0 to 10
for i in range(0,11,2):
    print(i)
    
#wap to print sum of first 5 natural number
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)


#using for loop print even  no between 50 and 70

for i in range(50,71,2):
    print(f"i:{i}")
print("bye")

#using for loop print 5 to 1

for i in range(5,0,-1):
    print(f"i:{i}")
print("bye")

#print no from 99 to 91
for i in range(99,90,-1):
    print(f"i:{i}")
print("bye")

#print odd number . from 19 to 1

for i in range(19,0,-2):
    print(f"i:{i}")
print("bye")

#print even numbers.from 10 to 0

for i in range(10,0,-2):
    print(f"i:{i}")
print("bye")

#accept a number and print factorial of number using foor loop

num=int(input("enter number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"factorial:",fact)


#wap to accept 5 subject marks using for loop and print total and percentage and grade

total=0
for i in range(1,6):
    marks=int(input("enter subject marks:"))
    total=total+marks
print(f"total marks {total}")
per=total=(total/500)*100
print(f"percentage {per}")

if per>=75:
    print("distinction")
elif per>=60 and per<75:
    print("first grade")
else:
    print("fail")
    
       
# wap to accept number and print table of that number using for loop(print multiplication table)

num=int(input("enter number:"))
for i in range(1,11):
    print(f"{num} x {i}={num*i}")
    
    
#wap to print total of first 5 natural numbers using for loop(natural no are (1 ---------------all)
total=0
for i in range(1,6):
    total=total+i
print("total of first 5 natural numbers:", total)
    
       
#wap to print sum of first 5 natural numbers using for loop
  
sum=0
for i in range(1,6):
    sum=sum+i
print(f"sum of first 5 natural numbers:{sum}")
'''
#program to print sum of even no between 1 to 10
sum=0
for i in range(0,11):
    if(i%2==0):
         sum=sum+i
print(sum)

#program to print sum of odd no between 1 to 10
sum=0
for i in range(1,11):
    if(i%2!=0):
       sum=sum+i
print(sum)
    
#program to print factorial of 5
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#program to accept 3 subject marks and calculate total marks using for loop
sum=0
for i in range(1,4):
    marks=int(input("enter marks:"))
    sum=sum+marks
print("total marks:",sum)
per=(total/300)*100
print("percentage:",percentage)
if per>=75:
    print("distinct")
elif per>=60 and per<75:
    print("first grade")
else:
    print("fail")






