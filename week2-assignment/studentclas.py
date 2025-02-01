class Student:
    def __init__(self):
        self.name=input("Enter student name:")
        self.roll_num=input("Enter roll number:")
    def get_details(self):
        print("The student details are")
        print(f"Name:{self.name}\nRoll_Num:{self.roll_num}")
o=Student()
o.get_details()