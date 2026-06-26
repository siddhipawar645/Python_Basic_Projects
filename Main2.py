try:
    mark1=int(input("Enter marks1:"))
    mark2=int(input("Enter marks2:"))
    mark3=int(input("Enter marks3:"))
    mark4=int(input("Enter marks4:"))
    mark5=int(input("Enter marks5:"))
    list=[mark1,mark2,mark3,mark4,mark5]
    total=mark1+mark2+mark3+mark4+mark5
    print("Total Marks:",total)
    avg=total/5
    print("Average:",avg)
    ("Highest Marks:",max(list))
    ("Lowest Marks:",min(list))
    list.sort()
    print("Sorting List:",list)
except ValueError:
    print("Error:Please enter an integer value")

