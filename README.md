# Secure Cryptography System  
**Network & Data Security Course Project**

## 📌 Overview

This project is a simplified secure communication system that demonstrates the core concepts of modern cryptography, including:

- ✅ RSA public key cryptography  
- ✅ Public Key Infrastructure (PKI) with a Certification Authority (CA)  
- ✅ Authenticated Diffie-Hellman key exchange (MITM protection)  
- ✅ Digital signatures  
- ✅ A custom-designed Feistel block cipher  
- ✅ ISO/IEC-style padding  

The system simulates secure communication between two users (**User A** and **User B**) under the supervision of a trusted **Certification Authority (CA)**.

All cryptographic components are implemented manually without using external cryptography libraries, as required by the project specification.

---

## 🏗 System Architecture

The project is organized into modular components:

```
core/        → Cryptographic primitives (RSA, DH, hashing, signatures)
models/      → User, CA, Certificate, DH message structures
symmetric/   → Feistel cipher, padding, binary converters
ui/          → Command-line interface
main.py      → Program entry point
```

### Main Entities

- **CA (Certification Authority)**
  - Generates RSA key pair
  - Issues digital certificates for users
  - Verifies certificates

- **User A & User B**
  - Generate RSA key pairs
  - Receive certificates from CA
  - Perform authenticated Diffie-Hellman
  - Encrypt and decrypt messages using a shared master key

---

## 🔐 Security Workflow

### 1️⃣ System Initialization
- CA generates RSA keys
- Users A and B generate RSA keys
- CA issues digital certificates
- Users verify their certificates using CA's public key

### 2️⃣ Authenticated Diffie-Hellman
- Users generate DH private/public values
- Each public value is digitally signed
- Certificates and signatures are verified
- A shared secret is computed
- A 16-bit `master_key` is derived

✅ This prevents Man-in-the-Middle (MITM) attacks.

---

### 3️⃣ Symmetric Encryption (Feistel Cipher)

A custom 16-bit block cipher is implemented using:

- 4 Feistel rounds
- XOR with round keys
- 4×4 S-Box
- 8-bit P-Box permutation
- ISO/IEC-style padding

Messages are:
1. Converted to binary
2. Padded
3. Split into 16-bit blocks
4. Encrypted using the derived master key

Decryption reverses the process.

---

## 🧠 Educational Objectives

This project demonstrates:

- How RSA key generation works (prime selection, φ(n), modular inverse)
- How digital signatures are created and verified
- How certificates bind identity to public keys
- Why Diffie-Hellman alone is vulnerable to MITM
- How authentication prevents active attacks
- How block ciphers operate internally (Feistel structure)
- Bitwise operations in cryptography

---

## ▶️ How to Run

```bash
python main.py
```

Follow the interactive menu:

1. Initialize system  
2. Establish shared key  
3. Encrypt message (A → B)  
4. Decrypt message (B)  
5. Show system status  
6. Exit  

---

## ⚠️ Important Notes

- This project is for **educational purposes only**.
- Small prime ranges and simplified hashing are intentionally used.
- The system is **not secure for real-world usage**.
- No external cryptography libraries were used.

---

## 📚 Technologies Used

- Python 3
- Pure built-in functions only
- Bitwise arithmetic (`^`, `>>`, `&`)
- Modular exponentiation (`pow(base, exp, mod)`)

---

## ✅ Project Status

✔ Fully functional  
✔ Authenticated key exchange  
✔ Successful encryption & decryption  
✔ MITM protection implemented