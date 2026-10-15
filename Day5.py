'''customer segment classification (retail / E-commerce)
situation: you are analyzing customer spending data. based on total purchese amount in the last 6 months, classify the customer
into segment for targeted marketing.
rules:
>=50,000->"premium"
20,000-49,999->"gold"
5,000-19,999->"silver"
<5,000->"bronze"
'''
purchase_amount=float(input("enter total purchase amount:"))
if purchase_amount >=50000:
    segment="premium"
elif purchase_amount >=20000 and purchase_amount <=49999:
    segment="gold"
elif purchase_amount >=5000 and purchase_amount <=19999:
    segment="silver"
else:
    segment="bronze"
print(f"customer segment :{segment}")

print("------------------------------------------------------------------------------------")


'''sales performance rating (sales team analysis)
situation:a data analyst needs to rate a salesperson's monthly performance based on target achivement percentage.
Rules: >=120%->"outstanding"
100%-119%->"excellent"
80%-99%->"good"
50%->"needs improvement"
'''

target= float(input("enter monthly target:"))
achived= float(input("enter actual sales:"))
percentage=(achived / target)*100

if percentage >=120:
    rating= "outstanding"
elif percentage >=100:
    rating= "excellent"
elif percentage >=80:
    rating= "good"
elif percentage >=50:
    rating= "average"
else:
    rating=" needs improvement"
print(f"achivement:{percentage:.2f}%")
print("performance rating:",rating)

print("************************************************************************************************************")

'''product discount category(pricing analysis)
situation: you are analyzing inventory and need to decide the discount  category for a product based on  its current stock
level.
Rules:
stock<=10->"clearance sale(40% off)"
stock 11-30->"heavy discount(25% off)"
stock 31-100->"regular discount(10% off)"
stock>100->"no discount"
'''

stock=int(input("enter current stock quality:"))
if stock<=10:
    discount="clearance sale(40% off)"
elif stock<=30:
    discount="heavy discount(25% off)"
elif stock<=100:
    discount="regular discount(10% off)"
else:
    discount="no discount"
print("recomendation:",discount)








        