from symmetric.converter import text_to_binary, binary_to_text, split_blocks
from symmetric.padding import apply_padding, remove_padding

P_BOX = [7, 3, 5, 1, 6, 2, 4, 0]
S_BOX = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]

def generate_round_keys(master_key):
    keys = []
    for i in range(1, 5): 
        k = ((master_key >> i) ^ (master_key >> (i + 4))) & 0xFF
        keys.append(k)
    return keys

def apply_sbox(x):
    left = S_BOX[(x >> 4) & 0xF]
    right = S_BOX[x & 0xF]
    return (left << 4) | right

def apply_pbox(x):
    result = 0
    for i in range(8):
        bit = (x >> i) & 1
        result |= bit << P_BOX[i]
    return result

def F(r, k):
    return apply_pbox(apply_sbox(r ^ k))

def feistel_encrypt(block, master_key):
    L = (block >> 8) & 0xFF
    R = block & 0xFF
    keys = generate_round_keys(master_key)
    for k in keys:
        L, R = R, L ^ F(R, k)
    return (R << 8) | L

def feistel_decrypt(block, master_key):
    L = (block >> 8) & 0xFF
    R = block & 0xFF
    keys = generate_round_keys(master_key)[::-1]
    for k in keys:
        L, R = R, L ^ F(R, k)
    return (R << 8) | L

def encrypt_message(text, master_key):
    binary = text_to_binary(text)
    padded = apply_padding(binary)
    blocks = split_blocks(padded, 16)
    encrypted = []
    for b in blocks:
        encrypted.append(feistel_encrypt(int(b, 2), master_key))
    return encrypted

def decrypt_message(blocks, master_key):
    binary = ""
    for b in blocks:
        dec = feistel_decrypt(b, master_key)
        binary += format(dec, "016b")
    unpadded = remove_padding(binary)
    return binary_to_text(unpadded)