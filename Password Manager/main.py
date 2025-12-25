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
    hashed_master_pass = hash_password(master_password) # the SHA-256 algo will convert this into hash hex string 
    user_data = {'user_name': user_name, 'master_password': hashed_master_pass} # then we store the user data in dictionary
    file_name = 'user_data.json' #this is the file name where the user's data will go and be saved 

    if os.path.exists(file_name): # if the file already exists then overwrite it
        with open(file_name, 'w') as file:
            json.dump(user_data, file) # put the user_data into the json file 
            print("\n[+] Registration complete!!\n")
    else:
        with open(file_name, 'x') as file: # if does not exists then create one 
            json.dump(user_data, file) #put the user_data into the json file
            print("\n[+] Registration complete!!\n")

#Function to encrypt a password.
def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode()).decode()

# Function to decrypt a password.
def decrypt_password(cipher, encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def login(username , entered_password):
    try:
        with open('user_data.json', 'r') as file: #reading file user_data.json
            user_data = json.load(file)           #loading file by json.load into user_data variable
        
        stored_password_hash = user_data.get('master_password')
        entered_password_hash = hash_password(entered_password)

        if stored_password_hash == entered_password_hash and username == user_data.get('user_name'):
            print("\n[+] Login Successful...\n")
        else:
            print("\n[-] Invalid login credentials. Please use the credentials you used to register.\n")
            sys.exit()
    except Exception:
        print("\n[-] You have not registered. Please do that. \n")
        sys.exit()


def view_websites():
    try:
        with open('password.json', 'r') as data:
            view = json.load(data)

            print("\nWebsites you saved...\n")

            for x in view:
                print(x['website'])
            print('\n')
    
    except FileNotFoundError:
        print("\n[-] You have not saved any passwords!\n")
    


    