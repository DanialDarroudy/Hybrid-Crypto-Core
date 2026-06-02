from models.certificate import Certificate


class CA:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_rsa_keys(self):
        pass

    def issue_certificate(self, user) -> "Certificate":
        pass

    def verify_certificate(self, certificate) -> bool:
        pass
