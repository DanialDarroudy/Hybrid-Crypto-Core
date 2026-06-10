def simple_hash(data: str) -> int:
    h = 0
    for b in data.encode():
        h ^= b
    return h
