import random

def is_prime(x: int) -> bool:
     x_sqrt = int(x**(1/2)) + 1
     for i in range(2, x_sqrt+1):
          if x % i == 0:
               return False
     return True     

def extended_euclidean(a: int, b: int):
        if b==0 :
            return a, 1, 0
        g, x_old, y_old = extended_euclidean(b, a%b)
        x = y_old
        y = x_old - y_old * (a//b)
        return g, x, y
    
    

def mod_inverse(e: int, phi: int) -> int:
    g, x, y = extended_euclidean(e, phi)
    return x % phi
    


def generate_rsa_keys():
    interval_primes = []
    for x in range(50,200):
         if is_prime(x):
              interval_primes.append(x)
    
    p = random.choice(interval_primes)
    interval_primes.remove(p)
    q = random.choice(interval_primes)
    n = p*q
    phi = (p-1)*(q-1)
    e = 257
    d = mod_inverse(e, phi)
    
    return {
            "p": p,
            "q": q,
            "n": n,
            "phi": phi,
            "public_key": (n, e),
            "private_key": (n, d),
        }



def rsa_encrypt(message: int, public_key: tuple) -> int:
    n , e = public_key
    return pow(message, e, n)


def rsa_decrypt(cipher: int, private_key: tuple) -> int:
    n, d = private_key
    return pow(cipher, d, n)

