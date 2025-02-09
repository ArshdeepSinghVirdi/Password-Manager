from modules.encryption import password_decrypt
from modules.paths import ENC_PASS_FILE, ENC_PASS_KEY_FILE


def get() -> bytes:
    with open(ENC_PASS_KEY_FILE, "rb") as f:
        content = f.read()
        f.close()
    encrypted_password_key = content

    with open(ENC_PASS_FILE, "rb") as f:
        content = f.read()
        f.close()
    encrypted_password = content

    return password_decrypt(encrypted_password_key,
                            encrypted_password.decode()).decode()
