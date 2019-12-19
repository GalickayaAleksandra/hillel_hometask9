class Patron(object):
    BOOK_LIMIT = 3

    def __init__(self, name):
        self._name = name
        self._numBooks = 0

    def __str__(self):
        text = self._name + " has checked out " + \
               str(self._numBooks) + " books"
        return text

    def getName(self):
        return self._name

    def getNumBooks(self):
        return self._numBooks

    def incBooks(self):
        if self._numBooks < Patron.BOOK_LIMIT:
            self._numBooks += 1
        else:
            return 'Patron has reached his/her book limit'

    def decBooks(self):
        if self._numBooks <= 0:
            return 'Patron has no books checked out'
        else:
            self._numBooks -= 1
