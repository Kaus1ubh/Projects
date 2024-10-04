from cryptography.fernet import Fernet
import getpass
import os

#i know generate key is not a hundred percent secure, but signature checking gets the job done -  kaustubh
def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_master_password(password):
    key = load_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    with open("master.enc", "wb") as enc_file:
        enc_file.write(encrypted_password)

def decrypt_master_password():
    key = load_key()
    cipher = Fernet(key)
    with open("master.enc", "rb") as enc_file:
        encrypted_password = enc_file.read()
    return cipher.decrypt(encrypted_password).decode()

generate_key()

if not os.path.exists("master.enc"):
    new_password = getpass.getpass("Set a new master password: ")
    encrypt_master_password(new_password)
    print("Master password set successfully!")

master_password = getpass.getpass("Enter master password: ")
if master_password != decrypt_master_password():
    print("Incorrect master password!")
    exit()

print("Access granted!")
