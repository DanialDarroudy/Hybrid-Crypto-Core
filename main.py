from models.user import User
from models.ca import CA
from ui.menu import show_menu


def main():
    ca = CA()
    user_a = User("A")
    user_b = User("B")

    while True:
        show_menu()
        choice = input("Choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("Goodbye 😊")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")
        
        print("\n")


if __name__ == "__main__":
    main()
