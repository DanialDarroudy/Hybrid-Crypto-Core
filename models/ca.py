from models.certificate import Certificate
from core.rsa import *


class CA:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_rsa_keys(self):
        rsa_keys = self.generate_rsa_keys()
        self.public_key = rsa_keys["public_key"]
        self.private_key = rsa_keys["public_key"]

    def issue_certificate(self, user) -> "Certificate":
        pass

    def verify_certificate(self, certificate) -> bool:
        pass
