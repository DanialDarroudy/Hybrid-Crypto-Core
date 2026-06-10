from models.certificate import Certificate
from core.rsa import generate_rsa_keys
from core.signature import sign, verify


class CA:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_rsa_keys(self):
        rsa_keys = generate_rsa_keys()
        self.public_key = rsa_keys["public_key"]
        self.private_key = rsa_keys["private_key"]

    def issue_certificate(self, user) -> "Certificate":
        n, e = user.public_key
        data = f"{user.user_id}{n}{e}"
        signature = sign(data, self.private_key)
        return Certificate(user.user_id, n, e, signature)

    def verify_certificate(self, certificate: Certificate) -> bool:
        data = certificate.data_to_sign()
        return verify(data, certificate.ca_signature, self.public_key)
