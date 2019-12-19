class Library(object):
    def __init__(self, name):
        self._name = name
        self._patrons = {}
        self._books = {}

    def __str__(self):
        text = "Library: " + self._name + '\n' + \
               "Books:   " + str(len(self._books)) + '\n' + \
               "Patrons: " + str(len(self._patrons))
        return text

    def addBook(self, book):
        self._books[book.getTitle()] = book

    def removeBook(self, book_title):
        try:
            self._books.pop(book_title)
        except Exception:
            print('Book not found in Library \"' + self._name + '\"')

    def findBook(self, book_title):
        try:
            return self._books[book_title]
        except Exception:
            print('Book not found in Library \"' + self._name + '\"')

    def addPatron(self, patron):
        self._patrons[patron.getName()] = patron

    def removePatron(self, patron_name):
        try:
            self._patrons.pop(patron_name)
        except:
            print('Patron not found in Library \"' + self._name + '\"')

    def findPatron(self, patron_name):
        try:
            return self._patrons[patron_name]
        except Exception:
            print('Patron not found in Library \"' + self._name + '\"')

    def listPatrons(self):
        return '\n'.join(map(str, self._patrons.values()))

    def listBooks(self):
        return '\n'.join(map(str, self._books.values()))

    def getName(self):
        return self._name
