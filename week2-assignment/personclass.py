class Person:
    def show(self):
        print("Iam person")
class Employee(Person):
    def work(self):
        print("Iam Employee")
class manager(Employee):
    def show(self):
        print("Iam manager")
    def approve_leave(self):
        print("I can approve the leaves of employees in my company")
o2=manager()
o2.work()
o2.show()
o2.approve_leave()