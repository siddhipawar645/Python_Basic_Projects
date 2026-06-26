student={}
def student_database():
    while True:
        try:
            print("****Student Information****")
            print("1.Add Student Info")
            print("2.Search Student Info")
            print("3.Display Student Info")
            print("4.Exit")
            ch=int(input("Enter your choice:"))
            if ch==1:
                    def student_add_info():
                        print("****ADD STUDENT INFO****")
                        name=input("Enter Student Name:")
                        roll=int(input("Enter Roll No:"))
                        age=int(input("Enter Student Age:"))
                        city=input("Enter Student City Name:")
                        student.update({
                        roll:{
                            " name":name,
                            "Roll No":roll,
                            "Age":age,
                            "City":city
                        }
                        }
                        )
                        print("***Student Info Added Successfully....***") 
                    student_add_info()    
            elif ch==2:
                    def student_search_info():
                        print("****SEARCH STUDENT INFO****")
                        roll=int(input("Enter Student Roll to Search Student Info:"))
                        if roll in student:
                                print("Student Name:",student.items())
                                print("***STUDENT INFO SEARCH SUCCESSFULLY...***")
                        else:
                                print("No Student Data Found...")
                    student_search_info()  
            elif ch==3:
                def view_all():
                 print("****DISPLAY STUDENT INFO****")   
                 if student: 
                    for roll,details in student.items(): 
                        print("Roll No:",roll,details) 
                 else: 
                    print("No student info found..!")  
                view_all()   
            elif ch==4:
                print("You can exit....") 
            else:
                print("Please try again....")
        except:
             print("Please enter valid info...")              
student_database()      
