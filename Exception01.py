try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = 0

    c = a / b
    print(c)
except:
    print("Division by zero is not allowed, Enter the numbers Again")
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = a / b
    print(c)
else:
    print("Program Executed successfully")
