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
            ca.generate_rsa_keys()
            print("CA RSA keys generated.")

            user_a.generate_rsa_keys()
            print("User A RSA keys generated.")

            user_b.generate_rsa_keys()
            print("User B RSA keys generated.")

            user_a.certificate = ca.issue_certificate(user_a)
            print("Certificate issued for user A")

            user_b.certificate = ca.issue_certificate(user_b)
            print("Certificate issued for user B")

            a_certificate_vefication = ca.verify_certificate(user_a.certificate)
            print(f"User A certificate verification: {a_certificate_vefication}")

            b_certificate_vefication = ca.verify_certificate(user_b.certificate)
            print(f"User B certificate verification: {b_certificate_vefication}")

        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
