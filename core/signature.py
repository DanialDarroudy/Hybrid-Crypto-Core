from core.hash import simple_hash


def sign(data: str, private_key: tuple) -> int:
    n, d = private_key
    h = simple_hash(data) % n
    return pow(h, d, n)


def verify(data: str, signature: int, public_key: tuple) -> bool:
    n, e = public_key
    expected_hash = simple_hash(data) % n
    decrypted_hash = pow(signature, e, n)
    return expected_hash == decrypted_hash
