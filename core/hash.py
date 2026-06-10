def simple_hash(data: str) -> int:
    hash = 0
    for byte in data.encode():
        hash ^= byte
    return hash
