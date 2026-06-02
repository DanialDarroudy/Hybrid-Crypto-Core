from models.dh_message import DHMessage
P = 65521
G = 11


def generate_private_value():
    pass


def compute_public_value(private_value: int) -> int:
    pass


def compute_shared_key(their_public: int, my_private: int) -> int:
    pass


def derive_master_key(k: int) -> int:
    return K % (2 ** 16)
