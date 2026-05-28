# Hybrid-Crypto-Core 🛡️

A high-performance cryptographic simulation built from scratch in Python. This project demonstrates a complete secure communication pipeline, integrating both symmetric and asymmetric cryptography without relying on external crypto libraries.

## 🚀 Key Features

- **Custom Public Key Infrastructure (PKI):** Implementation of a simulated Certificate Authority (CA) for identity verification and digital certificates.
- **Asymmetric Encryption (RSA):** Full implementation of RSA for secure key exchange and digital signatures (Key generation, prime numbers, and modular arithmetic).
- **Symmetric Block Cipher (Feistel):** A custom 4-round Feistel network for efficient and secure message encryption.
- **Key Exchange:** Secure session key establishment using the Diffie-Hellman (DH) protocol.
- **Zero Dependencies:** All cryptographic primitives are implemented using pure Python to demonstrate deep understanding of the underlying mathematics.

## 🏗️ System Architecture

The project simulates a real-world secure handshake and messaging flow:
1. **Registration:** Users register with the **CA** and receive signed certificates (RSA).
2. **Handshake:** Two parties authenticate each other and exchange a shared secret via **Diffie-Hellman**.
3. **Secure Messaging:** Messages are encrypted/decrypted using the **Feistel Cipher** with the shared session key.

## 🛠️ Technologies Used
- **Language:** Python 3.x
- **Concepts:** Modular Arithmetic, Prime Number Generation, Padding (PKCS7 style), Bitwise Operations.

## 📂 Project Structure
- `CA/`: Logic for the Certificate Authority and digital signatures.
- `Ciphers/`: Implementation of RSA and the 4-round Feistel network.
- `Protocol/`: Diffie-Hellman key exchange and session management.
- `main.py`: Interactive CLI to simulate the entire process.

## 📝 How it Works
1. Run `python main.py`
2. Generate RSA keys for the CA and Users.
3. Perform the authenticated Diffie-Hellman exchange.
4. Send encrypted messages between simulated users.

---
*This project was developed as part of a Cryptography course to demonstrate the practical application of secure protocols.*
