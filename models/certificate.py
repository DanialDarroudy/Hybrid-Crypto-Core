class Certificate:
    def __init__(self, user_id: str, n: int, e: int, ca_signature: int):
        self.user_id = user_id
        self.n = n
        self.e = e
        self.ca_signature = ca_signature

    def data_to_sign(self) -> str:
        return f"{self.user_id}{self.n}{self.e}"
