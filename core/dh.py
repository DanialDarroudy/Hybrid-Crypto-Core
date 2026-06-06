import random
from models.dh_message import DHMessage

P = 65521
G = 11

def generate_private_value() -> int:
    return random.randint(2, P - 2)

def compute_public_value(private_value: int) -> int:
    return pow(G, private_value, P)

def compute_shared_key(their_public: int, my_private: int) -> int:
    return pow(their_public, my_private, P)

def derive_master_key(k: int) -> int:
    return k % (2 ** 16)
