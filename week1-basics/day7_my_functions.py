#Day 7 My personal Function library

# Square a number
import re


def square(x):
    return x*x
print(square(5))

#Check if the number is positiv
def is_positive(number):
    if number>0:
      return "Positive"
    elif number<0:
        return "Negative"
    else:
        return "Zero"
print(is_positive(0))   

#Test your own functions

#Function Nr. 1
def greet_user(name):
    """ Greet user by name"""
    return f"Hello {name}!"
print(greet_user("Telman"))

#Function Nr. 2
def calculate_age_in_day(years):
    """Convert days in approximate days"""
    return years * 365
print(calculate_age_in_day(48))