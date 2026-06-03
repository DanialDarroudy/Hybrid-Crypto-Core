P_BOX = [7, 3, 5, 1, 6, 2, 4, 0]
S_BOX = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]


def generate_round_keys(master_key: int) -> list:
    round_keys = []
    for i in range(1, 5):
        ki = ((master_key >> i) ^ (master_key >> (i + 4))) & 0xFF
        round_keys.append(ki)
    return round_keys


def apply_sbox(x: int) -> int:
    h = S_BOX[(x >> 4) & 0x0F]
    l = S_BOX[x & 0x0F]
    return ((h << 4) | l) & 0xFF


def apply_pbox(value: int) -> int:
    result = 0
    for i in range(8):
        bit = (value >> P_BOX[i]) & 1
        result |= (bit << i)
    return result


def round_function(r: int, ki: int) -> int:
    x = r ^ ki
    tmp = apply_sbox(x)
    return apply_pbox(tmp)


def feistel_encrypt(block: int, master_key: int) -> int:
    left = (block >> 8) & 0xFF
    right = block & 0xFF
    keys = generate_round_keys(master_key)

    for key in keys:
        temp = right
        right = left ^ round_function(right, key)
        left = temp

    return (right << 8) | left


def feistel_decrypt(block: int, master_key: int) -> int:
    left = (block >> 8) & 0xFF
    right = block & 0xFF
    keys = generate_round_keys(master_key)
    keys.reverse()

    for key in keys:
        temp = right
        right = left ^ round_function(right, key)
        left = temp

    return (right << 8) | left


def encrypt_message(text: str, master_key: int) -> list:
    from symmetric.converter import text_to_binary, split_blocks
    from symmetric.padding import apply_padding

    bin_str = text_to_binary(text)
    padded_bin = apply_padding(bin_str)
    blocks = split_blocks(padded_bin, 16)

    encrypted_blocks = []
    for blk in blocks:
        blk_int = int(blk, 2)
        enc_int = feistel_encrypt(blk_int, master_key)
        encrypted_blocks.append(enc_int)

    return encrypted_blocks


def decrypt_message(encrypted_blocks: list, master_key: int) -> str:
    from symmetric.converter import binary_to_text
    from symmetric.padding import remove_padding

    decrypted_bin_str = ""
    for blk_int in encrypted_blocks:
        dec_int = feistel_decrypt(blk_int, master_key)
        dec_bin = format(dec_int, '016b')
        decrypted_bin_str += dec_bin

    unpadded_bin = remove_padding(decrypted_bin_str)
    return binary_to_text(unpadded_bin)
