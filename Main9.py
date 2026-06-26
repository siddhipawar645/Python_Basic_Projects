import math
def arithmetic():
    try:
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        ch=int(input("Enter your choice: "))
        if ch==1:
            print("Addition:",a+b)
        elif ch==2:
            print("Subtraction:",a-b)
        elif ch == 3:
            print("Multiplication:",a*b)
        elif ch == 4:
            print("Division:",a/b)
        else:
            print("Invalid Choice")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid Input.")
def scientific():
    try:
        num=float(input("Enter a number: "))
        print("1. Square Root")
        print("2. Power")
        print("3. Factorial")
        ch=int(input("Enter your choice: "))
        if ch==1:
            print("Square Root =",math.sqrt(num))
        elif ch==2:
            p = int(input("Enter power: "))
            print("Answer =",math.pow(num, p))
        elif ch==3:
            print("Factorial =",math.factorial(int(num)))
        else:
            print("Invalid Choice")
    except ValueError:
        print("Invalid Input.")
while True:
    print("\n***** SMART CALCULATOR *****")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        arithmetic()
    elif choice==2:
        scientific()
    elif choice==3:
        print("Thank You...!")
        break
    else:
        print("Invalid Choice")