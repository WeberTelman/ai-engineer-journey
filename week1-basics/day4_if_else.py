#Day 4 If-else statements

#1. Simple if Statement
age  = 20
if age>=18:
    print("You are an adult")

#2.IF-ElSE statement
score = 85
if score >=90:
    print("Grade: A")
else:
    print("Grade lower than A")      

#3. IF-ELIF-ELSE (Multiple conditions)
score = 85
if score >=90:
    print ("Grade: A")
elif score >=80:
    print ("Grade: B")
elif score >=70:
    print ("Grade: C")
else:
    print ("Grade: F")    

#4. Comparison Operator
x=10
y= 5

print(f"{x}=={y}: {x==y}")
print(f"{x}!={y}: {x!=y}")
print (f"{x}>{y}: {x>y}")
print (f"{x}<{y}: {x<y}")
print (f"{x}>={y}: {x>=y}")
print (f"{x}<={y}: {x<=y}")

#5. And Operator
age = 25
is_employed= True
if age >= 18 and is_employed:
    print ("You can apply for loan")
else:
    print ("You cannot apply yet for loan")    

# 6 OR Operator (At least one condition must be true)
has_car  = False
has_license  = True
if has_car or has_license:
    print ("You can drive (or will be able)")
else:
    print ("You cannot drive!")

#7. NOT Operator (Reverse the condition)
is_raining = False
if not is_raining:
    print("Let's go outside.")
else:
    print ("Stay inside!")

#8. Nested Loop (If inside another if)
age = 25
income = 5000

if age >=18:
    if income >=4000:
        print ("You qualify for credit card")
    else:
        print ("Income too low")
else: 
    print ("Too young")


#9. User input with IF-ELSE
name = input("What is your name?")
if name == "Alice":
    print("Hello Alice! Welcome back!")
elif name=="Bob":
    print ("Hello Bob! Long time no see.")
else:
    print(f"Hello {name}! Nice to meet you!")

#10 Temperature examle
temperature = 75
if temperature >80:
    print("It's hot. Wear light clothes")
elif temperature>60:
    print("It's nice. Perfect weather")
elif temperature >40:
    print("It's cool. Bring a jacket")
else:
    print("It's cold. Wear a coat")
