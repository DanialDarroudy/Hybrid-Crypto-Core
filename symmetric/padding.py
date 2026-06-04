def apply_padding(binary_string: str) -> str:
    binary_string += "10000000"
    while len(binary_string) % 16 != 0:
        binary_string += "0"
    return binary_string


def remove_padding(binary_string: str) -> str:
    index = binary_string.rfind("10000000")
    if index != -1 and all(c == '0' for c in binary_string[index + 8:]):
        return binary_string[:index]
    return binary_string
