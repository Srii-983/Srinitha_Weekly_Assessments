class Book:
    def __init__(self):
        self.title=input("Enter title of the book:")
        self.author=input("Enter author name:")
        self.isbn=int(input("enter isbn number:"))
    def book_details(self):
        print("The book details")
        print(f"Title: {self.title}\nAuthor: {self.author}\nIsbn Number: {self.isbn}")
o=Book()
o.book_details()