# from Books import *
from Control import *


def main():
    try:
        library_name = input("Please enter the name of the Library:  ")

        if not library_name:
            raise BadName
        lib = Manager(library_name)

        print('\n Thanks! :)')
    except Exception:
        print('There was a problem somewhere!')


main()
