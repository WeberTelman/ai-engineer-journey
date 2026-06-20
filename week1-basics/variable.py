"""
#name = "Telman";
age = 48
print(name, age)
#this is inline comment 
print(type(age)==int)
print(type(name))
print(isinstance(name, str))

age1  = 2
print(isinstance(age1,float))
age2 = float(2)
print(isinstance(age2, float))
age3 = "20"
print(isinstance(age3, int))
age4 = int("20")
print(isinstance(age4, int))
number = "20"
age5 = int(number)
print(isinstance(age5, int))

#complex for  complex number
#bool for booleans
#list for list
#tuple for tuples
#range for ranges
#dict for dictionaries
#set for sets

import enum
from operator import truediv
from random import SystemRandom
from traceback import print_tb
import webbrowser


condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 # False
condition1 or condition2# True


& performs binary AND
| performs binary OR
^ performs a binary XOR operation
~ perfoms a binary NOT operation
<< shift left operation
>> shif riht operation
is  identiy opertor, returns True if both Objects are the same
in membership operator, returns Triu if a values is contained in a list 

name = "Telman"
name += " is may name" # Telman is my name


print("telman".upper().lower())
print("tELmaN person".title().islower())


isalpha() to check if a string contains only of characters and is not empty
islanum() to check if a string conatains characters or digits and is not empty
isdecimal() to check if a sting contains digits and is not empty
lower() to get a lowercase version of a string
upper() to get an uppercase verson of a string
isupper() to check if a string is uppercase
title() to get a capitalized version of a string
startswith() to check if a string starts with specific substring
endswith() to check if a string ends with specific substring
replace() to replace a part of a string
split() to split a string into a specific character separator
strip() to trim the white space from the string 
join() to append new letters to a string
find() to find a positon of a substring



name2  = 'Weber  is \"AI Engineer\" and\n\'good \\ person\''
print(name2.lower())
print (name2)
print(len(name2))
print ("eb" in name2)

print(name2)

name3 = 'Telman Weber'
print(name3[0:6])
print(name3[:8])
print(name3[7:])



done1 = True
if done1:
    print ('yes')
else: 
    print('no')
    
done2 = 0   # equivalent to false, all other numbers are true
if done2: 
    print ('yes')
else: print ('no')

done3 = 'String' # not empty string is always true, empty string is always false
if done3:
    print ('yes')
else:
    print ('no')



done4 = False   
print (type(done4)== bool)

book_1_read = False
book_2_read = True
read_any_book = any([book_1_read, book_2_read])  # return true if any of items is true
read_any_book2=all([book_1_read, book_2_read]) 


num1 = 2+3j
num2 = complex(2,3)

print(num1.real, num2.imag)
print(type(num1))

print (round(5.49, 1)) # 5.5 rounding number and indicating how many decimal should be displayed


from enum import Enum

class State(Enum): 
    INACTIVE = 0
    ACTIVE= 1
print (State.ACTIVE) # =   print(State(1))  = print(State[ACTIVe])
print (State.ACTIVE.value)
print(list(State))
print(len(State))

#print("What is your age?")
#age = input()
#print("Your age is "+ age)

#age2 = input("What is your age? ")
#print ("Your age is "+ age2)


condition = False
firstName = "Syd"
if condition==True: 
    print("The conditon")
    print("was true")
elif firstName== "Roger":
    print("Hello Roger")
elif firstName == 'Syd':
    print ("Hello Syd")
else:
    print("The conditon")
    print("was false")


# List

dogs= ["Rogger", 50, 'Syd', True, "Kate", "Tomas"]    
print ("Kashtan" in dogs)
print(dogs[1])

dogs[0]="Layka"
print(dogs)
print(dogs[-2])
print(dogs[2:4])
print(len(dogs))

dogs.append('Alisa')
print(len(dogs))
dogs.extend(['Bob', 8]) # the same dogs+=['Bob', 8]
dogs+="Jane"
print(dogs)

dogs.remove('Alisa')
print(dogs)
dogs.pop()  # remove and return the last item
print(dogs)

items = ['Rogger', 1, 'Syd', True, 'Quincy', 7]
items.insert(2, 'Test')
print(items)

items[1:1] = ["TTTT", 'WWW']
print(items)

items2 = ['Syd', 'Rogger', 'Quincy', 'rogger']
items2.sort(key=str.lower)
print(items2)

itemsCopy = items2[:]
print (itemsCopy)

print(sorted(items2, key = str.upper))  #sorting without modifying original list
print(items2)

#Tuples
names = ('Rogger', 'Syd', 'Bob')
names[0]
names.index('Rogger')
len(names)
print('Rogger' in names)
print(names)
print(sorted(names))
newTuple = names + ("tina", 'Alice')
print(newTuple)


#Dictionaries
dog = {'name': 'Roofer', 'age': 8 }
print(dog)

print(dog['name'])

dog['name'] = 'Syd'
print(dog)
print(dog.get('name'))

print(dog.get('color', 'brown'))
print(dog.pop('name')) # return and remove the first item
print(dog)

print(dog.popitem()) # return and remove last item
print(dog)

dog2 = {'name': 'Roofer', 'age': 8 }
print('color' in dog2)
print(dog2.keys())
print(list(dog2.keys()))

print(dog2.values())
print(list(dog2.values()))
print(list(dog2.items()))
print(len(dog2))

dog2 ['favorint food'] = 'Meat'
print(dog2)

del dog2 ['age']
print(dog2)
dogCopy = dog2.copy()
print(dogCopy)


#Sets  - they are like Tuple, but they are unordered, and immutble. Set cannot have the same items

cats1 = {'Alisa', 'Markis'}
cats2 = {'Alisa'}
intersect = cats1 & cats2
print(intersect)

mod = cats1 | cats2  # union 2 sets
print(mod)

mod = cats1 - cats2 # get the difference between 2 sets
print(mod)

print(list(cats1))

#Functions

def hello():
    print("Hello!")

hello()

def helloName(name):
    print("Hello "+ name)
helloName("Telman")

def helloFried(name = "my friend"):
    print("Hello "+name)
helloFried()  


def helloNameOld(name, age):
    print("Hello " + name + ", you are "+ str(age) + " years old!")

helloNameOld("Telman", 48)


def change(value):
    value =2
val = 1
change(val)
print(val)

# but using Dictionhy show the value is mutatable
def change(value):
  value["name"] = "Syd"
  
val = {"name": "Telman"}
change(val)
print(val)  

def hello1(name):
    if not name:
        return
    print("Hello " +name +"!")
hello1("Telman")    


def hello2(name): 
    print("Hello "+ name+ "!")
    return name, "Telman", 50
print(hello2("Teo"))    


# Variable scope
age = 8 # global variable
def test():
    print(age)

print(age) #8
test()#8


#def test1():
#    age1 = 8
 #   print(age1)

#print(age1) #8
#test1()#8


#Nested function

def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(" ")
    for word in words:
        say(word)    
talk('I am goint to buy milk')        

# Nested function
def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(" ")
    for word in words:
        say(word)    
talk('I am goint to buy milk')        


def count():
    count = 0

    def increment():
        nonlocal count
        count = count+1
        print(count)
    increment()
count()                



def counter():
    count = 0

    def increment():
        nonlocal count
        count = count+1
        return count
    return increment

increment = counter()
print(increment())     
print(increment())  
print(increment())            




# Objects   Everything in Python is Object
# Objects has attributes and methods

age = 8

print(age.real)
print(age.imag)
print(age.bit_length())

items = [1, 2]
items.append(3)
items.pop()
print(id(items))


#Loops

from itertools import count

# while loop
condition = True
while condition == True:
        print("The conditon is true")
        condition = False



count = 0
while count< 10:
    print("The condition is true")
    count +=1
print("After Loop ")    


# For loop
items = [1,2,3,4]
for item in items:
    print(item)


for item in range(15):
    print(item)




items = [1,2,3,4]
for index, item in enumerate(items):
    print(index, item)


items = ["Telman","Jeyla","Lyaman","Ahad"]
for index, item in enumerate(items):
    print(index, item)


items = [1,2,3,4]
for item in items:
    if item==2:
     continue
    print(item)    

items = [1,2,3,4]
for item in items:
    if item==2:
     break
    print(item)      


#Classes

class Animal:
    def walk(self):
     print("walking...")

class Dog (Animal): 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof")

roger = Dog("Roger", 8)
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()

"""

#Modules - every python file is a Module
"""
math for math utilities
re for reqular expressions
json to work with json
datetime to work with dates 
sqlite3 to use sqlite 
os for Operating System utilities
random for random generation
statistics for statistics utilities
request to perform HTTP network _Request 
http to create HTTP service 
urllib to manage URLs 


import math
import sys
import argparse
print(math.sqrt(4))

# Accepting Arguments

parser = argparse.ArgumentParser (
    description="this program prints the name of my dog"
)

parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red', 'yello'}, help='the colo to search for')

args = parser.parse_args()

print(args.color)





#Lambda functions
from tokenize import Double


lambda num : num*2

multiply = lambda a,b: a*b

print(multiply(2,4))

# map(), filter(), reduce()

#map()
numbers = [1,2,3]

#def double (a):
#    return a*2
# or we can use lambda function
double  = lambda a: a*2

result = map(double, numbers)
# or we can use lambda function directly in map 
result = map(lambda a: a*2, numbers)

print(list(result))



#filter

numbers = [1,2,3,4,5,6,7,8]
#def isEven(n):
#    return n%2==0
#result  = filter(isEven, numbers)


# or we can use lambda directly in filter function
result  = filter(lambda a: a%2==0, numbers)

print(list(result))    

from functools import reduce
#reduce
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

#sum=0
#for expense in expenses:
#    sum+= expense[1]

# we can use reduce function instead of foreach loop
sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)    



#Recursion 
#3!= 3*2*1
#4!= 4*3*2*1
#5!= 5*4*3*2*1

def factorial (n):
    if n==1: return 1
    return n*factorial(n-1)    
print(factorial(3))
print(factorial(4))
print(factorial(5))



#Decorators

def logtime(func):
    def wrapper():
        print ('before')
        val = func()
        print ('after')
        return val
    return wrapper


@logtime    
def hello ():
    print('Hello')

hello()    



#Docstrings
def increment(n):
#    Incremennt a number
#    return n+1


 Dog module
This module does bla bla bla  and provides the follwing cases: 

- Dog
...




class Dog:
     A class representing a dog 
    def __init__(self, name, age):
         Initializing a new dog 
        self.name = name
        self.age = age
    def bark(self):
        Let the dog bark 
        print("WOF!")


print(help(Dog))


#Annotations

def increment (n: int)-> int:
    return n+1

count: int = 0



#Exeptions

try:
    # some line of code
except  <Error1>:
    # handle Error 1
except <Error2>:
    # nadle Error 2 
#except:  # all errors          
else:
    # no exceptions were raised, the code ran successfully
finally:
    # do something in any case 


from math import exp


try: result= 2/0
except ZeroDivisionError: 
    print ('Cannot divide by 0')
finally:
    result = 1    
print(result)

try:
    raise Exception ('An error!')
except Exception as error:
 print (error)        


 class DogNotFountException(Exception):
    print('inside')
    pass

try: 
    raise DogNotFountException()
except DogNotFountException:
    print ('Dog not found')    

    

#List compressions

numbers = [1,2,3,4,5]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)



# Polymorhpism

class Dog: 
    def eat (self):
        print('Eating dog food')

class Cat: 
    def eat(self):
        print('Eating cat food')

animal1= Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()
    

"""    

# Operator overloading

import operator


class Dog: 
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __gt__(self, other):
        return True if self.age>other.age else False    

roger =Dog('Roger', 8)
syd =Dog('Syd', 7)

print(roger<syd)

__add__() respond to the + operator
__sub__() respond to the - operator
__mul__() respond to the * operator
__truedif__() respond to the / operator
__floordif__() respond to the // operator
__mod__() respond to the % operator
__pow__() respond to the ** operator
__rshift__() respond to the >> operator
__lshift__() respond to the << operator
__and__() respond to the & operator
__or__()  respond to the | operator
__xor__() respond to the ^ operator 

