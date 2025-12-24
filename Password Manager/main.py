import json, hashlib, getpass, os, pyperclip, sys
from cryptography.fernet import Fernet

Master_password = input("Set the master password to open password manager")

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()

# Generate a secret key
def generate_key():
    return Fernet.generate_key()

#Initialize Fernet cipher with the provided key
def initialize_cipher(key):
    return Fernet(key)


def register(user_name , master_password):
    #Encrypt the master password before storing it
    hashed_master_pass = hash_password(master_password)
    user_data = {'user_name': user_name, 'master_password': hashed_master_pass}
    file_name = 'user_data.json'

    if os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump(user_data, file) 
            print("\n[+] Registration complete!!\n")
    else:
        with open(file_name, 'x') as file:
            json.dump(user_data, file)
            print("\n[+] Registration complete!!\n")

#Function to encrypt a password.
def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode()).decode()

# Function to decrypt a password.
def decrypt_password(cipher, encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def register()

database = {} #account : password

def view():
    pass

def add():
    pass

def main():
    while True:
        user_choice = input("Now you have entered the password manager what you like to do view passwords or set password.(/view, /add, /q (quit) )")

        if user_choice == '/q':
            print("Quiting...")
            break

        if user_choice == "/view":
            view()

        elif user_choice == "/add":
            add()

        else:
            print("You have typed wrong command, commands (/view , /add, /q)")


    