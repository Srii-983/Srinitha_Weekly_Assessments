from abc import ABC,abstractmethod
class IDatabase(ABC):
    @abstractmethod
    def insert(self):
        pass
    def delete(self):
        pass
    def update(self):
        pass
class SQLDatabase(IDatabase):
    def insert(self):
        print(" Record is inserted")
    def delete(self):
        print("Record is deleted")
    def update(self):
        print("Table is updated")
class NOSQLDatabase(IDatabase):
    def insert(self):
        print("Record is inserted")
    def delete(self):
        print("Record is deleted")
    def update(self):
        print("Table is updated")
m=SQLDatabase()
m.insert()
m.delete()
m.update()
n=NOSQLDatabase()
n.insert()
n.delete()
n.update()