# Proyecto 3: Biblioteca


class Author:

    def __init__(self, name, surnames):

        self.Name = name
        self.Surnames = surnames

    def showAuthor(self):

        print("Name: ", self.Name, "\nSurname(s): ", self.Surnames)


class Book:

    def __init__(self, title, ISBN):

        self.Title = title
        self.ISBN = ISBN

    def addAuthor(self, author):

        self.Author = author

    def showBook(self):

        print('------------ Book ------------')
        print("Title: ", self.Title, "\nISBN: ", self.ISBN)
        self.Author.showAuthor()
        print('------------ Book ------------\n\n')

    def obtainTitle(self):

        return self.Title

class Library:

    def __init__(self):

        self.Books = []

    def numberofBooks(self):

        print("There is a total of", len(self.Books), "books in this library")

    def addBook(self, book):

        self.Books = self.Books + [book]

    def eraseBook(self, title):

        found = False
        index = -1

        for books in self.Books:
            index += 1
            print(index)
            if books.obtainTitle() == title:
                found = True
                break
        if found:
            print(index)
            del self.Books[index]
            print('The Book',title,'has been removed from the Library')
        else:
            print('The Book', title,'has not been found')

    def showLibrary(self):

        print('------------ List of Books in the Snake Library ------------\n\n')
        for books in self.Books:
            books.showBook()
        print('------------ List of Books in the Snake Library ------------\n\n')



def showMenu():

    print('''
    *********************\n
    Welcome to the Snake Library!\n
    *********************\n''')

    print('Snake Library Menu\n\n'
          '1) Add a Book to the library\n'
          '2) Show the Librabry\'s content\n'
          '3) Erase a Book from the Librabry\n'
          '4) Show the number of books in the Library\n'
          '5) Exit\n')


def addaBooktotheLibrary(library):

    name = str(input("Write the author's name: "))
    surname = str(input("Write the author's surnames: "))
    title = str(input("What is the book's title? "))
    ISBN = str(input("ISBN: "))

    author = Author(name, surname)
    book = Book(title, ISBN)

    book.addAuthor(author)
    library.addBook(book)

    return library


def showLibrary(library):

    library.showLibrary()


def eraseBook(library):

    title = str(input('Write the book\'s name you wish to delete: '))
    library.eraseBook(title)


def numberofBooks(library):

    library.numberofBooks()


loop = False
library = Library()

while not loop:

    showMenu()
    choice = int(input('What would you like to do? '))

    if choice == 1:

        library = addaBooktotheLibrary(library)

    if choice == 2:

        showLibrary(library)

    if choice == 3:

        eraseBook(library)

    if choice == 4:

        numberofBooks(library)

    if choice == 5:

        print('Hope to see you soon again!')
        loop = True
