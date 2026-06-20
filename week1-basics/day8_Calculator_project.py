# Task 1.1 - Professional Calculator Program

# Define all Calculator functions
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract one number from another"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y != 0:
        return x / y
    else:
        return "Error: You cannot divide by zero"   

def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid Input! Please enter a valid number")

def display_menu():
    """Display operation menu"""
    print() 
    print("=" * 40)
    print("CHOOSE AN OPERATION")
    print("=" * 40)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("=" * 40)

def perform_calculation(operation_choice, num1, num2):
    """Perform the selected calculation"""
    if operation_choice == "1":
        result = add(num1, num2)
        operation = "+"
    
    elif operation_choice == "2":
        result = subtract(num1, num2)
        operation = "-"

    elif operation_choice == "3":
        result = multiply(num1, num2)
        operation = "*"
    
    elif operation_choice == "4":
        result = divide(num1, num2)
        operation = "/"
    
    else:
        return None, None, None

    return result, operation, num1, num2

def display_result(num1, operation, num2, result):
    """Display the calculation result nicely"""
    print()
    print("=" * 40)
    print(f"CALCULATION: {num1} {operation} {num2}")
    print(f"RESULT: {result}")
    print("=" * 40)

def main():
    """Main calculator program"""
    print("=" * 40)
    print("Welcome to Professional Calculator")
    print("=" * 40)
    
    while True:
        # Display Menu
        display_menu()

        # Get user choice
        user_choice = input("Enter your choice (1/2/3/4/5): ")

        # Check if the user wants to exit
        if user_choice == "5":
            print()
            print("=" * 40)
            print("Thank you for using Calculator")
            print("Goodbye!")
            print("=" * 40)
            break
        
        # Validate choice
        if user_choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1, 2, 3, 4 or 5")
            continue

        # Get numbers from user
        print()
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        # Perform calculation
        result, operation, n1, n2 = perform_calculation(user_choice, num1, num2)

        # Display result
        if result is not None:
            display_result(n1, operation, n2, result)

        # Ask if the user wants to continue
        print()
        continue_choice = input("Press ENTER to continue, or type 'quit' to exit: ") 
        if continue_choice.lower() == 'quit':
            print()
            print("=" * 40)
            print("Thank you for using Calculator")
            print("Goodbye!")
            print("=" * 40)
            break

# Run the program
if __name__ == "__main__":
    main()