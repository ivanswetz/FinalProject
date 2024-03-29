import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair():
    p = random.randint(100, 1000)
    while not is_prime(p):
        p = random.randint(100, 1000)

    q = random.randint(100, 1000)
    while not is_prime(q) or q == p:
        q = random.randint(100, 1000)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    e, n = pk
    cipher = []
    for char in plaintext:
        ascii_value = ord(char)
        encrypted_char = pow(ascii_value, e, n)
        cipher.append(encrypted_char)
    return cipher

def decrypt(pk, ciphertext):
    d, n = pk
    plain = []
    for char in ciphertext:
        decrypted_char = pow(char, d, n)
        original_char = chr(decrypted_char)
        plain.append(original_char)
    return ''.join(plain)

if __name__ == "__main__":
    public, private = generate_keypair()
    message = input("Enter a message to encrypt: ")
    print("Original Message:", message)
    encrypted_msg = encrypt(public, message)
    print("Encrypted Message:", ''.join(map(lambda x: str(x), encrypted_msg)))
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)

