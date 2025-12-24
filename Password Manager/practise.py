import hashlib
from cryptography.fernet import Fernet


something = input("Enter something: ")

key = Fernet.generate_key()
Fernet(key)


sha256 = hashlib.sha256() # creating sha256 algorithm object
sha256.update(something.encode()) # converting string to bytes and feeding through update into sha256 algorithm
print(sha256.hexdigest())
print(key)