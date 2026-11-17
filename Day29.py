#MODULE Practice
#module is a built in file which contains functions, classes and variable, which can reused in any python program
#we write the code in this file and the code run on anoter file usingcal1
#types of module:1)builtin module(math, random,os)
                #2)third party modules (pandas, numpy, scikit-learn, pytorch)
                #3)user defined module(custom module)
#ex:
import math #math is built in module
print(math.pi)
print(math.sqrt(20))
print(math.cos(0))

#ex:
from math import sqrt as s, pi as p
print(p)
print(s(16))

#ex:random gives any random value
import random 
print(random.randint(1,10)) #random no aaynge output me 1 me se 10 ke bech integer no hi aaynge float me nhi


