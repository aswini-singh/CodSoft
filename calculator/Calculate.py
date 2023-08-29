import sys

# Define the arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:

    # Display operation choices to the user
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Perform the selected operation
    if choice == '1':
            # Get user input for two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))       
        print(f"{num1} + {num2} = ",add(num1,num2))

    elif choice == '2':
            # Get user input for two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} - {num2} = ", subtract(num1,num2))

    elif choice == '3':
            # Get user input for two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} * {num2} = ",multiply(num1,num2))

    elif choice == '4':
            # Get user input for two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} / {num2} = ",divide(num1,num2))
        
    else:
        print("Plz select correct operation ")
        sys.exit()
