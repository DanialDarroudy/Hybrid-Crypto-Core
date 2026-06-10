from models.user import User
from models.ca import CA
from ui.menu import show_menu
from core.signature import verify
import symmetric.feistel as feistel


def main():
    ca = CA()
    A = User("A")
    B = User("B")
    last_cipher = []

    while True:
        show_menu()
        choice = input("Choice: ")

        if choice == "1":
            print("\n[ system Initializing... ]")
            ca.generate_rsa_keys()
            print("CA RSA keys generated.")
            A.generate_rsa_keys()
            print("User A RSA keys generated.")
            B.generate_rsa_keys()
            print("User B RSA keys generated.")

            A.certificate = ca.issue_certificate(A)
            print("Certificate issued for User A by CA.")
            B.certificate = ca.issue_certificate(B)
            print("Certificate issued for User B by CA.")

            print(
                f"User A checks own Certificate: {'Valid' if ca.verify_certificate(A.certificate) else 'Invalid'}")
            print(
                f"User B checks own Certificate: {'Valid' if ca.verify_certificate(B.certificate) else 'Invalid'}")
            print("\n[+] System initialized successfully!")

        elif choice == "2":
            if not A.certificate:
                print("\n[!] Please run Option 1 first to initialize the system.")
                continue

            print("\n[ Establishing Shared Key & Authenticating... ]")
            A.generate_dh_values()
            B.generate_dh_values()

            msgA = A.create_dh_message()
            msgB = B.create_dh_message()

            is_valid_cert_from_A = ca.verify_certificate(msgA.certificate)
            is_valid_cert_from_B = ca.verify_certificate(msgB.certificate)
            if not is_valid_cert_from_A:
                print("\n[!] User A certificate is invalid.")
                continue
            if not is_valid_cert_from_B:
                print("\n[!] User B certificate is invalid.")
                continue

            is_valid_sign_A = verify(str(msgA.public_value), msgA.signature, (msgA.certificate.n, msgA.certificate.e))
            is_valid_sign_B = verify(str(msgB.public_value), msgB.signature, (msgB.certificate.n, msgB.certificate.e))

            if not is_valid_sign_A:
                print("\n[!] User A signature is invalid (MITM Detected!).")
                continue
            if not is_valid_sign_B:
                print("\n[!] User B signature is invalid (MITM Detected!).")
                continue

            A.compute_master(msgB.public_value)
            B.compute_master(msgA.public_value)
            print("Signatures Verified! MITM attack prevented.")
            print("\n[+] Shared Key Established Successfully!")
            print(f"    User A Master Key: {A.master_key}")
            print(f"    User B Master Key: {B.master_key}")

        elif choice == "3":
            if not A.master_key:
                print("\n[!] Please run Option 2 to establish a shared key first.")
                continue

            msg = input("\nEnter message to encrypt (User A): ")
            last_cipher = feistel.encrypt_message(msg, A.master_key)
            print(f"\n[+] Encrypted Blocks: {last_cipher}")
            print("    (These blocks are stored in memory for Option 4)")

        elif choice == "4":
            if not B.master_key:
                print("\n[!] Please run Option 2 first.")
                continue

            print("\n--- Decryption Process ---")
            print(f"Hint: Last encrypted blocks in memory are: {last_cipher}")
            cipher_input = input("Enter encrypted blocks separated by comma (or press Enter to use blocks in memory): ")

            if cipher_input.strip() == "":
                if not last_cipher:
                    print("\n[!] No blocks provided and memory is empty.")
                    continue
                blocks_to_decrypt = last_cipher
            else:
                try:
                    blocks_to_decrypt = [int(x.strip()) for x in cipher_input.split(',')]
                except ValueError:
                    print("\n[!] Validation Error: Please enter valid comma-separated integers.")
                    continue

            decrypted_msg = feistel.decrypt_message(blocks_to_decrypt, B.master_key)
            print(f"\n[+] Decrypted Message at User B: {decrypted_msg}")

        elif choice == "5":
            print("\n" + "=" * 20 + " SYSTEM STATUS " + "=" * 20)
            print(f"CA Public Key         : {ca.public_key if ca.public_key else 'Not Generated'}")
            print(f"User A Public Key     : {A.public_key if A.public_key else 'Not Generated'}")
            print(f"User B Public Key     : {B.public_key if B.public_key else 'Not Generated'}")
            print(f"User A Certificate    : {'Issued & Valid' if A.certificate else 'None'}")
            print(f"User B Certificate    : {'Issued & Valid' if B.certificate else 'None'}")
            print(f"User A Master Key     : {A.master_key}")
            print(f"User B Master Key     : {B.master_key}")
            print(f"Latest Encrypted Data : {last_cipher if last_cipher else 'None'}")
            print("=" * 55)

        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 6.")

        print("\n")


if __name__ == "__main__":
    main()