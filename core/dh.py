import random

P = 65521
G = 11


def generate_private_value():
    return random.randint(2, P - 2)


def compute_public_value(private):
    return pow(G, private, P)


def compute_shared_key(their_public, my_private):
    return pow(their_public, my_private, P)


def derive_master_key(k):
    return k % (2 ** 16)
