import hashlib
import hmac
import base64

from Crypto.Cipher import AES, DES, PKCS1_OAEP, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad



def md5(text):
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()


def sha256(text):
    m = hashlib.sha256()
    m.update(text.encode('utf-8'))
    return m.hexdigest()


text = '123456'
print(f'md5 of {text} is {md5(text)}')
print(f'sha256 of {text} is {sha256(text)}')



print(f"utf-8 encode of {text} is {text.encode('utf-8')}")
print(f"base64 encode of {text} is {base64.b64encode(text.encode('utf-8'))}")



def hmac_(data, key, method):
    hash_func = getattr(hashlib, method)
    __hmac = hmac.new(key.encode('utf-8'), data.encode('utf-8'), hash_func)
    return __hmac.hexdigest()

key = 'alicebob'
print(f'hmac sha256 with key {key} of {text} is {hmac_(text, key, "sha256")}')


# ------------------------------------------------------------------------------------- #
# DES
def des_encrypt(text, key, iv):
    cipher = DES.new(key.encode('utf-8')[:8], DES.MODE_CBC, iv.encode('utf-8')[:8])
    padded_text = pad(text.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return base64.b64encode(ciphertext).decode('utf-8')

def des_decrypt(text, key, iv):
    cipher = DES.new(key.encode('utf-8')[:8], DES.MODE_CBC, iv.encode('utf-8')[:8])
    padded_text = cipher.decrypt(base64.b64decode(text.encode('utf-8')))
    plaintext = unpad(padded_text, DES.block_size).decode('utf-8')
    return plaintext

des_key = 'eightbyt'  # DES key must be 8 bytes
des_iv = 'thievish'  # DES IV must be 8 bytes

des_encrypted_text = des_encrypt(text, des_key, des_iv)
print(f'DES encrypt of {text} is {des_encrypted_text}')

des_decrypted_text = des_decrypt(des_encrypted_text, des_key, des_iv)
print(f'DES decrypt of {des_encrypted_text} is {des_decrypted_text}')

# ------------------------------------------------------------------------------------- #
# AES
def aes_encrypt(text, key, iv):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    padded_text = pad(text.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return base64.b64encode(ciphertext).decode('utf-8')

def aes_decrypt(text, key, iv):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    padded_text = cipher.decrypt(base64.b64decode(text.encode('utf-8')))
    plaintext = unpad(padded_text, AES.block_size).decode('utf-8')
    return plaintext

aes_key = 'AESrequires16or24or32Byt'  # AES input 16/24/32 Bytes key.
aes_iv = 'ivshouldbe16byte'  # AES block size is 16 bytes, therefore iv should be 16 bytes

aes_encrypted_text = aes_encrypt(text, aes_key, aes_iv)
print(f'AES encrypt of {text} is {aes_encrypted_text}')
aes_decrypted_text = aes_decrypt(aes_encrypted_text, aes_key, aes_iv)
print(f'AES decrypt of {aes_encrypted_text} is {aes_decrypted_text}')

# ------------------------------------------------------------------------------------- #
# RSA
rsa_key = RSA.generate(2048)
rsa_public_key = rsa_key.publickey()
rsa_private_key = rsa_key
print(f"RSA public key is {rsa_public_key.exportKey('PEM')}")
print(f"RSA private key is {rsa_private_key.exportKey('PEM')}")

rsa_import_pubkey = RSA.importKey(open('public.pem').read())
print(f'Imported RSA public key is {rsa_import_pubkey.exportKey()}')

def rsa_encrypt(pubkey, text):
    cipher = PKCS1_OAEP.new(pubkey)
    encoded_text = cipher.encrypt(text.encode('utf-8'))
    return base64.b64encode(encoded_text).decode('utf-8')

def rsa_decrypt(privatekey, text):
    cipher = PKCS1_OAEP.new(privatekey)
    decoded_text = cipher.decrypt(base64.b64decode(text.encode('utf-8')))
    return decoded_text.decode('utf-8')

rsa_encrypted_text = rsa_encrypt(rsa_public_key, text)
print(f'RSA encrypt of {text} is {rsa_encrypted_text}')
rsa_decrypted_text = rsa_decrypt(rsa_private_key, rsa_encrypted_text)
print(f'RSA decrypt of {rsa_encrypted_text} is {rsa_decrypted_text}')


