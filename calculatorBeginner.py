print("################### Calculator #######################")

def add(a, b):
    return a + b 

def substract(a,b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b 

def floor_division(a, b):
    return a // b 

while True:
    try:
        num1 = float(input("\nEnter your first number "))
        num2 = float(input("\nEnter your second number "))
    except ValueError:
        print("\nPlease enter a valid real number")
        continue 
    
    operation = input("Enter your operation (+, -, *, /, //) ")
    if operation == "+":
        result = add(num1, num2)
        print(f"Your result: {result}")
    elif operation == "-":
        result = substract(num1, num2)
        print(f"Your result: {result}")
    elif operation == "*":
        result = multiply(num1, num2)
        print(f"Your result: {result}")
    elif operation == "/" and num2 == 0:
        print("Cannot divide by 0.")
        continue 
    elif operation == "/":
        result = divide(num1, num2)
        print(f"Your result: {result}")
    elif operation == "//" and num2 == 0:
        print("Cannot divide by 0.")
        continue 
    elif operation == "//":
        result = floor_division(num1, num2)
        print(f"Your result: {result}")
    else:
        print("\nPlease select a valid mathematical operation")
        continue 

    leave = str(input("Leave calculator? (y/n)")).lower()
    if leave in ['yes', 'y', 'ye']:
        break