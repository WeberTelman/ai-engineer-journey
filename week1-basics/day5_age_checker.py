#Day 5 Practice - interactive age checker

print("="*40)
print("AGE CHECKER PROGRAM")
print("="*40)

# Get user's age
age = int(input("How old are you?"))

#Check age and give feedback
if age<0:
    print("That is not valid age!")
elif age<13:
    print("Your are a child. Enjoy your childhood.")
elif age<18:
    print ("Your are a teenageer. Explore and learn.")
elif age<65:
    print("Your are an adult. Keep growing. ")
else:
    print("Your are a senior. Enjoy your wisdom.")


#Extra check
if age>=18:
    print("You can vote.")
    print("You can work.")
    print("You can get driver's license.")
else: 
    print("You cannot vote yet.")
    print("You have restrictions on work.")
    print("You cannnot get driver's license yet.")

    