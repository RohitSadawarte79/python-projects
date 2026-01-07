import hashlib,json,os



def hash_password(password):
    sha256 = hashlib.sha256()

    sha256.update(password.encode())
    
    return sha256.hexdigest()

print(hash_password("I am Rohit Sadawarte, I am amazing and one thing I know I can do anything means anything you know"))
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

register("Rohit79", "qwerty@212005")

