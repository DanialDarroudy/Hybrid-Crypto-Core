class User:
    def __init__(self, name: str):
        self.name = name
        self.public_key = None
        self.private_key = None
        self.certificate = None
        self.master_key = None
        self.dh_private = None
        self.dh_public = None

    def generate_rsa_keys(self):
        pass

    def generate_dh_values(self, p: int, g: int):
        pass

    def sign_value(self, value: int):
        pass

    def compute_shared_key(self, other_public: int, p: int):
        pass
