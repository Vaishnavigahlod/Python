#TUPLE
'''
#ex:1)with bracket is explicit
num=(1,2.2,"hello",True)
print(type(num))
print(num[0])
for i in num:
    print(i)
num1=(11,)
print(type(num1))

#ex:2)without bracket is implicit
num=1,2.2,"hello"
print(type(num))
for i in num:
    print(i)
    
#ex:3)-1 used to get last no of tuple
num=1,2.2,"hello"
print(type(num))
print(num[-1]) #use -1 to get last element of tuple
'''

#SLICing

#ex:slice
    #0 1 2 3 4    indexing 
num=(1,2,3,4,5)
print(num)
print(num[1:4])
print(num[:3])
print(num[3:])
print(num[::2])
print(num[::-1])