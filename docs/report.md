# 1. Algorithm Description

This project implements a hybrid cryptographic communication system that combines asymmetric cryptography (RSA and PKI), authenticated Diffie–Hellman key exchange, and a symmetric block cipher based on a Feistel network. The goal is to simulate a secure message exchange protocol between two users (A and B) under the supervision of a Certification Authority (CA).

The system is divided into three major cryptographic components: RSA-based digital signatures and certificates, authenticated Diffie–Hellman key exchange, and symmetric encryption using a custom Feistel structure.

---

## 1.1 RSA and Public Key Infrastructure (PKI)

RSA is used in this project exclusively for authentication and digital signature purposes.

### Key Generation

Each entity (CA, User A, and User B) generates its own RSA key pair as follows:

1. Two prime numbers p and q are randomly selected from the interval [50, 200].
2. The modulus n is computed as n = p × q.
3. Euler’s totient function is calculated as phi(n) = (p − 1)(q − 1).
4. The public exponent e is fixed to 257, as required in the project specification.
5. The private exponent d is computed as the modular inverse of e modulo phi(n) using the Extended Euclidean Algorithm.

The public key is (n, e) and the private key is (n, d).

### Digital Signatures

A simple XOR-based hash function is used to produce a one-byte hash of input data. The signature process is:

1. Compute the hash of the input data.
2. Reduce the hash modulo n (if necessary).
3. Raise the hash to the power of d modulo n.

Verification is performed by raising the signature to the power of e modulo n and comparing the result with the recomputed hash of the received data.

### Certificate Authority (CA)

The CA simulates a basic Public Key Infrastructure. It performs the following tasks:

1. Generates its own RSA key pair.
2. Issues digital certificates for users A and B.
3. Verifies certificates when requested.

A certificate contains:
- User ID
- Public modulus n
- Public exponent e
- CA signature over the concatenation of (User ID, n, e)

The CA signs the certificate data using its private key. Any user can verify the authenticity of a certificate using the CA’s public key.

This mechanism ensures that public keys cannot be replaced by an attacker without detection.

---

## 1.2 Authenticated Diffie–Hellman Key Exchange

The system uses Diffie–Hellman (DH) to establish a shared symmetric key between User A and User B.

### Parameters

The public parameters are:
- Prime modulus P = 65521
- Generator G = 11

### Key Exchange Process

Each user performs the following:

1. Selects a random private value x in the range [2, P − 2].
2. Computes the public value Y = G^x mod P.
3. Signs the public value using their RSA private key.
4. Sends the tuple (Certificate, Public Value, Signature) to the other party.

Upon receiving this tuple, the receiver:

1. Verifies the certificate using the CA’s public key.
2. Extracts the sender’s public key from the certificate.
3. Verifies the signature on the Diffie–Hellman public value.
4. If verification succeeds, computes the shared secret:
   K = (Y_other)^x mod P

Finally, the master key is derived as:
master_key = K mod 2^16

This ensures the symmetric key fits into 16 bits, as required for the Feistel cipher.

The addition of RSA signatures to the DH public values prevents Man-in-the-Middle attacks. Without the private key of the legitimate user, an attacker cannot produce a valid signature.

---

## 1.3 Symmetric Encryption Using a Feistel Network

To ensure confidentiality of messages, a custom 16-bit Feistel block cipher is implemented.

### Message Preparation

1. The plaintext message is converted into its 8-bit ASCII binary representation.
2. ISO/IEC 7816-4 padding is applied:
    - A single byte 10000000 is appended.
    - Zero bits are appended until the total length becomes a multiple of 16 bits.
3. The padded message is split into 16-bit blocks.

### Feistel Structure

Each 16-bit block is divided into:
- Left half (8 bits)
- Right half (8 bits)

The cipher consists of 4 rounds.

### Round Key Generation

Four 8-bit round keys are derived from the 16-bit master key. Each round key is generated using bit shifts and XOR operations on the master key, ensuring deterministic but distinct keys for each round.

### Round Function

The round function F operates as follows:

1. XOR the right half with the round key.
2. Apply substitution using a predefined 4×4 S-box.
3. Apply permutation using an 8-bit P-box.

The Feistel transformation for each round is:
- New Left = Right
- New Right = Left XOR F(Right, Round Key)

After 4 rounds, the halves are swapped to produce the ciphertext block.

### Decryption

Decryption follows the same structure but uses the round keys in reverse order. Due to the Feistel design, the encryption and decryption algorithms are structurally identical.

After decrypting all blocks:
1. The binary string is reconstructed.
2. Padding is removed.
3. The binary data is converted back to ASCII text.

---

# 2. Security Analysis

This section evaluates the strengths and limitations of the implemented system from a security perspective.

---

## 2.1 Security Strengths

### Authentication and Integrity

The use of RSA-based digital signatures ensures:

- Only the legitimate owner of a private key can sign Diffie–Hellman parameters.
- Certificates bind public keys to user identities.
- Any modification of DH parameters or certificates is detected during verification.

This prevents impersonation and Man-in-the-Middle attacks during key exchange.

### Confidentiality

The Feistel network provides confidentiality through:

- Multiple rounds of substitution and permutation.
- Non-linear transformation via S-box.
- Bit diffusion through P-box.

These properties introduce confusion and diffusion, two essential principles of secure block cipher design.

### Proper Padding

Using ISO/IEC 7816-4 padding ensures:

- The original message length can be precisely recovered.
- Ambiguities caused by zero padding are avoided.
- Even full blocks receive an additional padding block, as required by the standard.

---

## 2.2 Security Limitations and Vulnerabilities

Although functionally correct, this implementation has several intentional weaknesses due to educational constraints.

### Small RSA Key Size

The RSA modulus n is extremely small because p and q are chosen from a small interval (50–200). This makes factorization trivial. In practice:

- RSA requires at least 2048-bit keys.
- The current implementation is vulnerable to brute-force factorization in negligible time.

### Weak Diffie–Hellman Parameters

The prime modulus P = 65521 is only 16 bits long. This makes the discrete logarithm problem computationally easy. In real systems:

- DH parameters must be at least 2048 bits.
- Otherwise, attackers can compute private exponents efficiently.

### Weak Hash Function

The XOR-based hash function is cryptographically insecure:

- Output size is only 8 bits (256 possible values).
- Collisions are extremely easy to find.
- XOR is linear and commutative, enabling message manipulation without changing the hash.
- Vulnerable to existential forgery attacks.

In practice, secure hash functions such as SHA-256 or SHA-3 must be used.

### Small Symmetric Key Size

The master key is reduced to 16 bits. This makes brute-force key search trivial:

- A 16-bit key space contains only 65,536 possibilities.
- An attacker can try all keys almost instantly.

Modern symmetric encryption requires at least 128-bit keys.

### ECB-like Block Processing

Each block is encrypted independently. This resembles Electronic Codebook (ECB) mode:

- Identical plaintext blocks produce identical ciphertext blocks.
- Structural patterns may leak information.

Secure implementations use modes like CBC or GCM with initialization vectors.

### Answers to the “Simple Hash Function” Section

### 1. Why is the XOR-based hash function vulnerable to existential forgery attacks?

The hash function implemented in this project simply XORs all input bytes and produces a **1-byte (8-bit)** output. This design has several serious structural weaknesses that make existential forgery attacks feasible:

#### 1) Extremely Small Output Space (Weak Collision Resistance)

The hash output is only **8 bits**, meaning it can produce only **256 possible values (0–255)**.

By the pigeonhole principle, if an attacker generates enough different messages, collisions are guaranteed. In practice, an attacker needs to try at most around 256 different messages to find another message that produces the same hash value as a legitimate one.

This makes it trivial to create two different messages with identical hash values.

---

#### 2) Commutativity of XOR

XOR has the property:

```
A XOR B = B XOR A
```

This means the order of bytes does not affect the final result.

For example:

- The hash of `"AB"`  
- The hash of `"BA"`

will be identical.

If a legitimate message `"AB"` is signed, an attacker can rearrange it to `"BA"` and reuse the original signature. Since the hash remains the same, the signature verification will incorrectly succeed.

---

#### 3) How Existential Forgery Becomes Possible

Suppose an attacker intercepts a valid message and its digital signature.

Because the hash function is weak:

- The attacker can modify the message (e.g., reorder characters).
- Or add pairs of identical bytes (since `x XOR x = 0`, they cancel out).
- Or craft a completely new message that results in the same 8-bit hash.

The attacker then attaches the original signature to the forged message.

Since signature verification checks only:

```
hash(message) == decrypted_signature
```

and the hash matches, the receiver incorrectly believes the forged message is authentic.

This is a classic example of existential forgery due to weak hashing.

---

### 2. Which hash functions are used in real-world systems and why?

In real-world cryptographic systems, standardized cryptographic hash functions are used, such as:

- **SHA-256**
- **SHA-512**
- **SHA-3**
- (Previously SHA-1, though now deprecated)

These hash functions provide essential security properties that our XOR-based hash does not:

---

#### 1) Collision Resistance

It is computationally infeasible to find two different messages that produce the same hash value.

For example, SHA-256 has a 256-bit output, meaning the hash space is enormous.

---

#### 2) Preimage Resistance

Given a hash value, it is computationally infeasible to reconstruct the original message.

In contrast, the XOR hash is linear and very predictable.

---

#### 3) Avalanche Effect

A secure hash function ensures that changing **even one bit** of the input causes about half of the output bits to change unpredictably.

Example:

```
"Hello"
"Hello."
```

The hashes will be completely different.

In the XOR-based hash, changing one byte only affects the corresponding XOR result in a linear way. There is no avalanche effect.

---

#### 4) Non-Linearity and Unpredictability

Modern hash functions are built using complex nonlinear transformations. There is no simple algebraic relationship between input blocks and output bits.

Our XOR hash is purely linear and therefore easy to manipulate.

---

### 3. What is the minimum hash output length required for 80-bit security?

The correct answer is:

**160 bits**

---

#### Explanation Using the Birthday Attack

When we say a system provides “80-bit security,” it means an attacker must perform approximately:

```
2^80 operations
```

to break it.

For hash functions, the most relevant attack is finding a **collision**.

Due to the birthday paradox, a collision in an N-bit hash function can typically be found in approximately:

```
2^(N/2) operations
```

To achieve 80-bit collision resistance:

```
2^(N/2) = 2^80
```

Therefore:

```
N / 2 = 80
N = 160
```

So, a hash function must produce at least **160-bit output** to provide 80-bit security against collision attacks.

This is why SHA-1 used a 160-bit output (although it is no longer considered secure today).

---

### Final Security Insight

The XOR-based hash function in this project is intentionally weak due to:

- Educational constraints
- Small RSA modulus size
- Simplicity requirements

It is **not cryptographically secure** and is vulnerable to:

- Collision attacks  
- Message manipulation  
- Existential forgery  

In real-world systems, cryptographically secure hash functions such as SHA-256 or SHA-3 must always be used.

---

## Conclusion of Security Evaluation

The implemented system correctly demonstrates the principles of:

- Public key cryptography
- Digital signatures
- Authenticated key exchange
- Symmetric block cipher design
- Padding standards

However, due to simplified parameters and a weak hash function, it is not secure for real-world use. The implementation should be considered an educational model illustrating cryptographic concepts rather than a production-ready secure communication protocol.