try:
    square=lambda x:x**2
    numbers=range(1, 21)
    squares=[]
    for i in numbers:
        squares.append(square(i))
    print("Squares:",squares)
    print("***Even Squares***")
    for i in squares:
        if i%2 == 0:
            print("Even Number:",i)
except:
    print("Error:Please enter valid info")