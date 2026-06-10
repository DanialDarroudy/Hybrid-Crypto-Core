def text_to_binary(text: str) -> str:
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary_string: str) -> str:
    chars = [chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8) if binary_string[i:i + 8]]
    return ''.join(chars)


def split_blocks(binary_string: str, block_size: int = 16) -> list:
    return [binary_string[i:i + block_size] for i in range(0, len(binary_string), block_size) if
            binary_string[i:i + block_size]]


def join_blocks(blocks: list) -> str:
    return ''.join(blocks)
