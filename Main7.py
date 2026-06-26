class Employee:
    def __init__(self, emp_id, name, details):
        self.Emp_id = emp_id
        self.Name = name
        self.Details = details
    def show_details(self):
        print("Employee ID:", self.Emp_id)
        print("Employee Name:", self.Name)
        print("Department:", self.Details[0])
        print("Salary:", self.Details[1])
        print("------------------------")
employees={}
for i in range(3):
    print("***Enter Details of Employee***")
    emp_id=int(input("Enter Employee ID:"))
    name=input("Enter Employee Name:")
    department=input("Enter Department:")
    salary=int(input("Enter Salary:"))
    details=(department,salary)
    employees[emp_id]=Employee(emp_id,name,details)
print("\n***** Employee Details *****")
for emp in employees.values():
    emp.show_details()