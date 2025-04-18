from models.library import Library
import system.interface_functions as sif

library1 = Library("Library")
library1.register("Bono", 1990, "bono@", "0000-AA", True)
library1.add_book("Book1", 1987, "SmartOne")
print("\nWelcome to the Library")

def run():
    while True:
        user_input = input("\nWelcome Visitor, select a number from the list below:\n1) Browsing books\n2) Login as member\n3) Register as new member\n4) Leave Library\n")
        match user_input:
            case '0':
                library1.list_members()
            case '1':
                sif.list_books_interface(library1)
            case '2':
                member_run()
            case '3':
                sif.register_interface(library1)
            case '4':
                print("Thank you for visiting, have a nice day!")
                break
            case _ :
                print("Not recognizable input, please select a number from the list provided.")

def member_run():
    user_input_email = input("\nEnter member email: ")
    user_input_ID = input("\nEnter member ID:\n")
    user_input_access = sif.login_interface(library1, user_input_ID, user_input_email)
    while True:
        match user_input_access:
            case True:
                user_input = input("\nWelcome member, select a number from the list below:\n1) Browsing books\n2) Login as librarian\n3) Add new book\n4) Borrow book\n5) Unborrow book\n6) Profile\n7) Logout\n")
                match user_input:
                    case '1':
                        sif.list_books_interface(library1)
                    case '2':
                        user_input_access_librarian = sif.login_librarian(library1, user_input_ID)
                        while True:
                            match user_input_access_librarian:
                                case True:
                                    user_input = input("\nWelcome Librarian, select a number from the list below:\n1) Browsing books\n2) ??\n3) Add new book\n4) Borrow book\n5) Unborrow book\n6) Profile\n7) Logout\n")
                                    match user_input:
                                        case '1':
                                            sif.list_books_interface(library1)
                                        case '2':
                                            pass
                                        case '3':
                                            sif.add_book(library1)
                                        case '4':
                                            sif.borrow_book(library1, user_input_ID)
                                        case '5':
                                            sif.unborrow_book(library1, user_input_ID)
                                        case '6':
                                            sif.profile(library1, user_input_ID)
                                        case '7':
                                            print("Logout successfully")
                                            break
                                case _:
                                    print("Wrong access")
                                    break
                    case '3':
                        sif.add_book(library1)
                    case '4':
                        sif.borrow_book(library1, user_input_ID)
                    case '5':
                        sif.unborrow_book(library1, user_input_ID)
                    case '6':
                        sif.profile(library1, user_input_ID)
                    case '7':
                        print("Logout successfully")
                        break
            case _:
                print("Wrong access ID")
                break

