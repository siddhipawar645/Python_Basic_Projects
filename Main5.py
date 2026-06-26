import random
import math
try:
    numbers=set()
    print("***Enter 10 numbers***")
    for i in range(10):
        num = int(input("Enter number:"))
        numbers.add(num)
    print("Unique Numbers(Set):", numbers)
    tup=tuple(numbers)
    print("Tuple:", tup)
    if len(tup)>=3:
        random_numbers=random.sample(tup, 3)
        print("3 Random Numbers:",random_numbers)
    else:
        print("Less than 3 unique numbers available.")
    total=sum(tup)
    print("Sum of Tuple Elements:",total)
    if total>=0:
        print("Square Root of Sum:",math.sqrt(total))
    else:
        print("Square root cannot be calculated for a negative sum.")
except ValueError:
    print("Invalid input! Please enter only integers.")
