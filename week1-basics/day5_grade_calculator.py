#Day 5 Bonus Grade calculator
print("="*40)
print("GRADE CALCULATOR")
print("="*40)

#Get score from user
score = int(input("Enter your test score(0-100)"))

#Determine Grade
if score >=90:
    grade ="A"
    description= "Excellent!"
elif score >=80:
    grade = "B"
    description = "Good job!"
elif score >=70:
    grade = "C"
    description = "Passing grade!"
elif score >=60:
    grade= "D"
    description ="Just passing!"
else:
    grade = "F"
    description="Need to improve!"

#Extra feedback
if score >=90:
    print("Oustanding perfomance!")
elif score >=80:
    print("Keep it up!")
elif score >=70:
    print("Study more for better grades!")
else:
    print("Reach out for help!")

print("="*40)