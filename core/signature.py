from core.hash import simple_hash

def sign(data: str, private_key: tuple) -> int:
    hash = simple_hash(data)
    n ,d = private_key
    return pow(hash, d, n)



def verify(data: str, signature: int, public_key: tuple) -> bool:
    expected_hash = simple_hash(data)
    n, e = public_key
    signature_hash = pow(signature, e, n)
    return expected_hash == signature_hash