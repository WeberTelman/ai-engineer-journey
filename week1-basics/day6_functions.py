#Day 6 Practice Functions

#Simple function (No parameters, no retur)
def greet():
    print("Hello, AI Engineer!")
greet()
greet()
greet()

print()


#Functions with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Bob")
greet_person("Alice")
greet_person("Telman")
print()

#Functions with multiple parameters

def add (x, y):
    result= x+y
    print(f"{x}+{y} = {x+y}")

add(5, 10)
add(15154, 665468)
print()

#Function with return value
def multiply (x, y):
    return x*y

result=multiply(5, 4)
print(f"5*4={result}")

result=multiply(7, 455)
print(f"7*455={result}")
print()

#Function that returns calculation
def calculate_average(num1, num2, num3):
    average = (num1+ num2 + num3)/3
    return average

avr = calculate_average(5, 8, 48)
print(f"Avarage is {avr}")
print()


#Function with conditional logic
def check_age(age):
    if age >=18:
        return "Adult"
    else:
        return "Minor"


age1 = check_age(48)
age2 = check_age(15)
print(f"Age 48: {age1}")
print(f"Age 15: {age2}")
print ()

#Function with multiple calculations
def calculator(x, y, operator):
    if operator=="add":
        return x+y
    elif operator== "substract":
        return x-y
    elif operator== "multiply":
        return x*y
    elif operator== "divide":
        if y!=0:
          return x/y
        else:
            return "Cannot divide by 0"
    else:
        return "Unnoknw operator"

print(f"20+10 = {calculator(20, 10, "add")}")
print(f"20-10 = {calculator(20, 10, "substract")}")
print(f"20*10 = {calculator(20, 10, "multiply")}")
print(f"20/10 = {calculator(20, 10, "divide")}")
print()
        

# Function that returns multiple values
def get_person_info(name, age):
    status = "Adult" if age >=18 else "Minor"
    message = f"{name} is {age} years old and is {status}"
    return name, age, status, message


name, age, status, msg = get_person_info("Alice", 17)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Status: {status}")
print(f"Message: {msg}")
print()

#Function with default parameters
def introduce(name, age = 25, city = "New York"):
    print(f"Hi, I am {name}")
    print(f"I am {age} years old")
    print(f"I live in {city}")
print()

print(introduce("Telman"))
print(introduce("Alice"))
print(introduce("Bob"))


#Function that calls another function

def is_adult(age):
    return age>=18

def can_vote(age):
    if is_adult(age):
        return "Yes you can vote"
    else:
        return "No, you are too young to vote"

print(can_vote(48))
print(can_vote(17))

