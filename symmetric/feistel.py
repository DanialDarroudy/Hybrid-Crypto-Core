P_BOX = [7, 3, 5, 1, 6, 2, 4, 0]

S_BOX = []


def generate_round_keys(master_key: int) -> list:
    round_keys = []
    for i in range(4):
        ki = ((master_key >> i) ^ (master_key >> (i + 4))) & 0xFF
        round_keys.append(ki)
    return round_keys


def apply_sbox(x: int) -> int:
    pass


def apply_pbox(value: int) -> int:
    pass


def round_function(r: int, ki: int) -> int:
    pass


def feistel_encrypt(block: int, master_key: int) -> int:
    pass


def feistel_decrypt(block: int, master_key: int) -> int:
    pass
