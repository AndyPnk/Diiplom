from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def sign(uid):
    with open(f'{uid}_priv.pem', 'rb') as key_file:
        priv_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    file_to_sign = f"{uid}.json"
    with open(file_to_sign, 'rb') as file:
        data = file.read()

    sign = priv_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    sign_file = f'{uid}.pem'
    with open(sign_file, 'wb') as sig_file:
        sig_file.write(sign)
