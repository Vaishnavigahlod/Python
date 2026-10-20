'''
#accept the number is prime number or not a primes number.
#(prime no jo koi table me nhi aate 2,3,5,7,11,13,17,19,23,29,31,37,41,43,41)
num=int(input("enter number:"))
for i in range(2,num):
    if num% i==0:
        print("num is not prime number")
        break
    #(chek if num is not divided by any between no.
if num==(i+1):
    print("num is prime no")


#program to print no. betwwen 1 and 20

for num in range(3,21):
    for i in range(2,num):
        if num%i==0:
            #print(f"{num} is not prime no")
            break
        #check if num is not divided by any between no
    if num==(i+1):
        print(f"{num}is prime no")
'''
#
principal=1000.0 #$1,000 starting amount
rate=0.05 #5% annual intrest rate
year=4
print(f"initial investment:{principal}")
  #(loop through each year from 1 to 4
for year in range(1,year+1):
    interest=principal*rate
    principal+=interest
    print(f"year{year}:balance=${principal:.2f}")
    
    
