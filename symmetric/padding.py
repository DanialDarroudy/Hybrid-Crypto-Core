def apply_padding(binary_string):
    binary_string += "10000000"
    while len(binary_string) % 16 != 0:
        binary_string += "0"
    return binary_string


def remove_padding(binary_string):
    idx = binary_string.rfind("10000000")
    if idx == -1:
        return binary_string
    return binary_string[:idx]
