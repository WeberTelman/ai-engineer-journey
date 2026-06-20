# Day 7 Practice Utility function

# Function 1-  Check if number is even or odd
def is_even(number):
    if number%2 ==0:
        return "Even"
    else:
        return "Odd"  

print("Number checks")
print(f"25 is {is_even(25)}")
print(f"10 is {is_even(10)}")
print(f"-47 is {is_even(-47)}")
print(f"565954 is {is_even(565954)}")
print()


#Function 2-  Find maximum of 3 numbers

def find_max(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print("Maximum numbers:")
print (f"Max of 5, 10, 3 is {find_max(5, 10, 3)}")
print (f"Max of 1654, 1468, 16467 is {find_max(1654, 1468, 16467)}")
print (f"Max of -654654, -54887, -6548787 is {find_max(-654654, -54887,-6548787)}")
print (f"Max of -654654, 25, -6548787 is {find_max(-654654, 25,-6548787)}")
print()

#Function 3-  Convert temperature
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5)+32
    return fahrenheit

print("Temperature conversion")
print(f"0°C = {celsius_to_fahrenheit(0)}")
print(f"20°C = {celsius_to_fahrenheit(20)}")
print(f"30°C = {celsius_to_fahrenheit(30)}")
print(f"32°C = {celsius_to_fahrenheit(32)}")

#Function 4-  Calculate Discount
def apply_discount(price, discout_percent):
    discount_amount = price*(discout_percent/100)
    final_price = price -discount_amount
    return final_price


print("Shopping Discounts")

original = 1657
discounted = apply_discount(original, 20)
print(f"Original: ${original}, discounted price ${discounted}")


#Function 5-  Check if password is strong
def is_password_strong(password):
    if len(password)<8:
        return "Weak(too short)"
    elif password.isdigit() or password.isalpha():
        return "Weak (only letter or number)"
    else: 
        return "Strong"

print("Password strength")
print(f"'abc': {is_password_strong('abc')}")     
print(f"'21326545': {is_password_strong('21326545')}")  
print(f"'asdfadasdasdf': {is_password_strong('asdfadasdasdf')}")   
print(f"'232324dasda3434sdf': {is_password_strong('232324dasda3434sdf')}")  


#Function 6-  Count vowels in a word
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count +=1
    return count

print("Vowel counter")
print(f"'Hello' has {count_vowels("Hello")} vowels")
print(f"'Python' has {count_vowels("Python")} vowels")
print(f"'Engineering' has {count_vowels("Engineering")} vowels")
print(f"'RTHNMBFGklcvb' has {count_vowels("RTHNMBFGklcvb")} vowels")