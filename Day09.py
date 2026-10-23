'''
#accept password calc len , how many digits, how many special character, if valid password.
password=input("enter password:")
d=0
s=0
l=len(password)
special="!@#$%"
print(f"length:{l}")
for p in password:
    if p.isdigit():
        d=d+1
    if p in special:
        s=s+1
print(f"digits:{d}")
print(f"special character:{s}")

if(l<8 or d>0):
    if(s>0):
        print(f"password is valid")
    else:
         print("password is not valid")
else:
        print("password is not valid")
  
'''  
#accept no. of product/item
noprod=int(input("enter no. of products:"))
total=0
gtotal=0
for i in range(1,noprod+1):
    print("---------------------------------")
    print(f"enter details for product:{i}")
   #(accept product price and quantity)
    prodname=input("enter product name:")
    price=float(input("enter product price:"))
    quantity=int(input("enter product quantity:"))
    total=price*quantity
    gtotal=gtotal+total
    print(f"total amount:{total}")
    print("---------------------------------")
print(f"grant total amount:{gtotal}")
