try:
  class Student():
   def __init__(self,name,roll_no,marks):
    self.Name=name
    self.Roll_no=roll_no
    self.Marks=marks
   def add_mark(self):
    mark1=int(input("Enter marks1:"))
    mark2=int(input("Enter marks2:"))
    mark3=int(input("Enter marks3:"))
    mark4=int(input("Enter marks4:"))
    mark5=int(input("Enter marks5:"))
    self.Markslist=[mark1,mark2,mark3,mark4,mark5]
   def get_average(self):
    total=sum(self.Markslist)
    print("Total Marks:",total)
    avg=total/5
    print("Average:",avg)
   def display_info(self):
    print("Name:",self.Name)
    print("Roll No:",self.Roll_no)
    print("Marks:",self.Markslist)
except:
 print("Invalid input...")
s1=Student("Siddhi",22,[])  
s1.add_mark()
s1.get_average()
s1.display_info()





 