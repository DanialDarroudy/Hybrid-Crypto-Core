from core.rsa import generate_rsa_keys
from core.dh import generate_private_value, compute_public_value, compute_shared_key, derive_master_key
from core.signature import sign
from models.dh_message import DHMessage


class User:
    def __init__(self, name):
        self.user_id = name
        self.public_key = None
        self.private_key = None
        self.certificate = None
        self.master_key = None
        self.dh_private = None
        self.dh_public = None

    def generate_rsa_keys(self):
        keys = generate_rsa_keys()
        self.public_key = keys["public_key"]
        self.private_key = keys["private_key"]

    def generate_dh_values(self):
        self.dh_private = generate_private_value()
        self.dh_public = compute_public_value(self.dh_private)

    def create_dh_message(self):
        signature = sign(str(self.dh_public), self.private_key)
        return DHMessage(self.certificate, self.dh_public, signature)

    def compute_master(self, other_public):
        shared = compute_shared_key(other_public, self.dh_private)
        self.master_key = derive_master_key(shared)
