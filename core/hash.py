def simple_hash(data: str) -> int:
    data_bytes = data.encode("utf-8")
    hash = 0
    for byte in data_bytes:
        hash ^= byte
    return hash