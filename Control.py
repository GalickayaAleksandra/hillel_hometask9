from Books import *
from Library import *
from Patron import *


class Manager(object):
    def __init__(self, library_name):
        self._library = Library(library_name)
        print(self._library.getName() + " Library Manager")
        print(self.drawSep())
        while True:
            print(self.drawMenu())
            print("Please enter a selection:")
            try:
                sel = int(input("@  "))
                if sel == 11:
                    print("Program ending")
                    break
                elif sel == 1:
                    self.createPatron()
                elif sel == 2:
                    self.removePatron()
                elif sel == 3:
                    self.listPatrons()
                elif sel == 4:
                    self.createBook()
                elif sel == 5:
                    self.removeBook()
                elif sel == 6:
                    self.listBooks()
                elif sel == 7:
                    self.checkout()
                elif sel == 8:
                    self.returnbook()
                elif sel == 9:
                    self.bookInfo()
                elif sel == 10:
                    self.patronInfo()
                else:
                    print("Bad input. Program ending")
                    break
            except Exception:
                print("Bad selection, try again")
            print(self.drawSep())

    def createLibrary(self, name):
        return Library(name)

    def drawSep(self):
        return "================================="

    def drawMenu(self):
        print("MAIN MENU")
        print(self.drawSep())
        text = "1.  Add a new patron:\n"
        text += "2.  Remove a patron:\n"
        text += "3.  List all patrons:\n"
        text += "4.  Add a new book:\n"
        text += "5.  Remove a book:\n"
        text += "6.  List all books:\n"
        text += "7.  Check out a book:\n"
        text += "8.  Return a book:\n"
        text += "9.  Get book information:\n"
        text += "10. Get patron information:\n"
        text += "11. Exit the library manager:\n"
        return text

    def createPatron(self):
        print(self.drawSep())
        print("Add a new patron")
        try:
            name = input("Patron Name@  ")
            if not name:
                raise Exception()
            self._library.addPatron(Patron(name))
            print('Patron added')
            print('\n')
        except Exception:
            print('\n')

    def listPatrons(self):
        print(self.drawSep())
        print("List all patrons")
        print(self._library.listPatrons())
        print('\n')

    def removePatron(self):
        print(self.drawSep())
        print("Remove a patron")
        try:
            name = input("Patron Name@  ")
            if not name:
                raise Exception()
            self._library.removePatron(name)
            print("Patron removed.")
            print('\n')
        except Exception:
            print('Patron could not be removed.')
            print('\n')

    def createBook(self):
        print(self.drawSep())

        print("Add a book")
        try:
            title = input("Book Title @  ")
            if not title:
                raise Exception()
            try:
                author = input("Book Author@  ")
                if not author:
                    raise Exception()
                self._library.addBook(Book(title, author))
                print('\n')

            except Exception:
                print('Error creating book (bad author name)')
                print('\n')
        except Exception:
            print('Error creating book (bad title)')
            print('\n')

    def removeBook(self):
        print(self.drawSep())
        print("Remove a book")
        try:
            title = input("Book Title@  ")
            if not title:
                raise Exception()
            self._library.removeBook(title)
            print('\n')

        except Exception:
            print('Cannot remove book')
            print('\n')

    def listBooks(self):
        print(self.drawSep())
        print("List all books")
        print(self._library.listBooks())
        print('\n')

    def checkout(self):
        print(self.drawSep())
        print("Check out book")

        try:
            book = self._library.findBook(input("Book Title @  "))
            try:
                patron = self._library.findPatron(
                    input("Patron Name@  "))
                book.checkout(patron)
                print('\n')

            except Exception:
                print('\n')

        except Exception:
            print('\n')

    def bookInfo(self):
        print(self.drawSep())
        print("Book info")

        try:
            book = self._library.findBook(input("Book Title@  "))
            print(book)

            if book.isCheckedOut():
                print("This book is checked out by " + book.getPatron())
                print('People on waitlist\n')
                book.showWaitlist()
        except Exception:
            print('\n')

    def returnbook(self):

        print(self.drawSep())
        print("Return a book")

        book = self._library.findBook(input("Book Title@  "))
        book.returnbook()
        print('\n')

    def patronInfo(self):
        print(self.drawSep())
        print("Patron information")

        try:
            patron = self._library.findPatron(
                input("Patron Name@  "))
            print(patron)
        except Exception:
            print('\n')
