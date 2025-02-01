class Employee:
    def __init__(self):
            self.name=input("Enter Name:")
            self.id=int(input("Enter Id"))
            self.dept=input("Enter department:")
            print(f"{self.name} {self.id} {self.dept}")
ob=Employee()
