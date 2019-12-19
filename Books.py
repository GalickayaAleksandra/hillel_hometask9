class Book(object):

    def __init__(self, title, author, patron=None):
        self._title = title
        self._author = author
        self._patron = patron
        self._waitlist = []
        self._checked_out = False

    def __str__(self):
        return self._title + " by " + self._author

    def getTitle(self):
        return self._title

    def getAuthor(self):
        return self._author

    def getPatron(self):
        return self._patron.getName()

    def showWaitlist(self):
        for item in self._waitlist:
            print(item.getName())

    def checkout(self, patron):

        if self.isCheckedOut():
            self._waitlist.append(patron)
            print('Book is checked out. ' + patron.getName() +
                  ' is now on the waitlist for this book')

        else:
            if patron.getNumBooks() < 3:
                patron.incBooks()
                self._patron = patron
                self._checkedOut = True
                print("This book is now checked out by " + patron.getName())

            else:
                print('This patron has too many books checked out already')

    def isCheckedOut(self):
        return self._checked_out

    def return_book(self):

        self._checked_out = False
        self._patron.decBooks()

        while True:
            if len(self._waitlist) > 0:
                new_patron = self._waitlist.pop(0)
                if new_patron.getNumBooks() < 3:
                    self.checkout(new_patron)
                    break
            else:
                break
