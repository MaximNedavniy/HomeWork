class Author:

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
        Library.authors.append(self)

    def __repr__(self):
        return repr(self.name)


class Book:

    number_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.number_books += 1
        author.books.append(self)

    def __repr__(self):
        return repr(self.name)


class Library:

    books = []
    authors = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr(self.name)

    def new_book(self, name: str, year: int, author: Author):
        return self.books.append(Book(name, year, author))

    def group_by_author(self, author: Author):

        return [i for i in self.books if i.author == author]

    def group_by_year(self, year: int):
        return [i for i in self.books if i.year == year]


Author_1 = Author("Stephen King", "USA", "21.09.1947")
Author_2 = Author("Taras Shevchenko", "Ukraine", "09.03.1814")
Library_1 = Library("Library_1")
Library_1.new_book("IT", 1986, Author_1)
Library_1.new_book("The Green Mile", 1996, Author_1)
Library_1.new_book("Kobzar", 1840, Author_2)
print(Library.books)
print(Library.authors)
print(Library_1.group_by_author(Author_1))
print(Library_1.group_by_year(1996))
print(Book.number_books)
