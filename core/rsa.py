import random
from typing import Any


def is_prime(x: int) -> bool:
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def extended_euclidean(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(e: int, phi: int) -> Any | None:
    g, x, _ = extended_euclidean(e, phi)
    if g != 1:
        return None
    return x % phi


def generate_rsa_keys():
    primes = [x for x in range(50, 200) if is_prime(x)]
    while True:
        p = random.choice(primes)
        q = random.choice(primes)
        if p == q:
            continue
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 257

        d = mod_inverse(e, phi)
        if d is None:
            continue

        return {
            "public_key": (n, e),
            "private_key": (n, d),
        }


def rsa_encrypt(message: int, public_key: tuple) -> int:
    n, e = public_key
    return pow(message, e, n)


def rsa_decrypt(cipher: int, private_key: tuple) -> int:
    n, d = private_key
    return pow(cipher, d, n)