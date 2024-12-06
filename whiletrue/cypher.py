import pickle
import base64
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

# Cargar la clave desde un archivo binario al inicio del programa
try:
    with open('./encryption.bin', 'rb') as source:
        key = source.read()  # Clave global, constante durante la ejecución
except FileNotFoundError:
    raise RuntimeError("Archivo de clave 'encryption.bin' no encontrado.")

# Función para cifrar datos
def encrypt(json: dict) -> str:
    global key
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

# Función para descifrar datos
def decrypt(ciphertext_b64: str) -> dict:
    global key
    ciphertext = base64.b64decode(ciphertext_b64)  # Decodificar de Base64 a bytes

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()

    # Descifrar y remover padding
    padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = PKCS7(128).unpadder()
    json = pickle.loads(unpadder.update(padded) + unpadder.finalize())

    return json
