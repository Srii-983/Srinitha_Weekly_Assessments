class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __add__(self, other):
        if isinstance(other, Book):
            return f"Book Series: '{self.title}' & '{other.title}' by {self.author}"
        return "Invalid Operation"

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book1 = Book(title="Ignited Minds",author= "A.P.J Kalam")
book2 = Book(title="Wings of Fire",author= "A.P.J Kalam")

series = book1 + book2
print(series)