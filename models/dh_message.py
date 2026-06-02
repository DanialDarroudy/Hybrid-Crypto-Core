class DHMessage:
    def __init__(self, certificate, public_value: int, signature: int):
        self.certificate = certificate
        self.public_value = public_value
        self.signature = signature
