import base64
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

# Funciones de cifrado y descifrado
def encrypt(json: dict, key: bytes) -> str:
    import pickle
    serialized = pickle.dumps(json)  # Serializar el diccionario
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()

    # Padding para ajustar al tamaño del bloque
    padder = PKCS7(128).padder()
    padded = padder.update(serialized) + padder.finalize()

    # Cifrado
    ciphertext = encryptor.update(padded) + encryptor.finalize()

    # Codificar en Base64 para enviar como JSON
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt(ciphertext_b64: str, key: bytes) -> dict:
    import pickle
    # Decodificar de Base64 a bytes
    ciphertext = base64.b64decode(ciphertext_b64)

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()

    # Descifrar y remover padding
    padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = PKCS7(128).unpadder()
    json = pickle.loads(unpadder.update(padded) + unpadder.finalize())

    return json
