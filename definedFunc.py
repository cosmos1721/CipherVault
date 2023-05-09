import os
import getpass
from cryptography.fernet import Fernet
import pickle
import time

# all defined variables
    
def keyEncrypt(Passkey, userId, key1=0):
    def midStr(userId):
        length = len(userId)
        mid = length // 2
        if length % 2 == 0:
            return userId[mid-1:mid+1]
        else:
            return userId[mid]
    fileCode = Passkey[0] + midStr(userId) + Passkey[-1]    #output1
    #(1st char of mas_passw + mid (1) of name + mid(2) of name + last char of mas_passw).key
    newKey = fileCode[0] + str(key1) + fileCode[-1]                           #output2
    return newKey, fileCode
 

def newMasterKey():
    os.system('clear||cls')
    pUser= userId = input("Write your user id: ")
    pPass=pseudoPasskey = getpass.getpass("Write your new master password \n please note:- add digits for more secure password: ")
    confirmPseudoPasskey = input("Confirm your new master password: ")
    if pseudoPasskey != confirmPseudoPasskey:
        print("userID and Password do not match. Please try again. \n")
        print("Redirecting to main menu in 2 seconds...")
        time.sleep(2)
        newMasterKey()
    else:
        key1 = Fernet.generate_key()  # major key
        mKey = Fernet(key1)
        keyf = key1.decode('utf-8')
        newKey, fileCode = keyEncrypt(pseudoPasskey, userId, keyf)  # returned value to a variable
        key2 = Fernet.generate_key()  # minor key for encryption of passwords
        pKey = mKey.encrypt(key2)  # convert values to bytes
        pseudoPasskey = mKey.encrypt(pseudoPasskey.encode())
        userIdf = mKey.encrypt(userId.encode())
        newKey = newKey.encode()
        keys_add = [[fileCode, userIdf, newKey, pseudoPasskey, pKey]]
        postKey = Fernet(key2)
        userId = postKey.encrypt(userId.encode())
        with open('key.key', 'ab') as keyFile:
            pickle.dump(keys_add, keyFile)
        print("User added successfully!")
        try:
            with open('password.bin', 'rb') as f:
                data = pickle.load(f)
        except FileNotFoundError:
            data = []

        while True:
            # Get user input
            new_ffile = {'checkFile': fileCode, 'check': userId, 'file': []}
            data.append(new_ffile)
            with open('password.bin', 'wb') as f:
                pickle.dump(data, f)
                break

        print("Database created or updated")
        time.sleep(1)
        print("Key file contents:\nUser ID:", pUser, '\nMaster password:', '*' * len(pPass)) 
        print("hold on tight, reloading...")
        time.sleep(2)  
def verify():
    global fileCode,userId, postKey
    userId = input("Write your user id: ")
    Passkey = getpass.getpass("Write your master password: ")
    fileCode = keyEncrypt(Passkey, userId)[1]
    path= './key.key'
    check =os.path.exists(path)
    if check!= True:
        print("no such database found, create a new account to access the database")
        time.sleep(1)
        print("Redirecting to main menu in a few seconds...")
        time.sleep(1)
        os.system('clear||cls')
    else:
        with open("key.key", "rb") as keys:
            while True:
                
                try:
                    obj = pickle.load(keys)
                    for info in obj:
                        if info[0] ==keyEncrypt(Passkey, userId)[1]:
                            fileCode=keyEncrypt(Passkey, userId)[1]
                            code1 = fileCode[0] 
                            code2=fileCode[-1]
                            key = info[2].decode()
                            key1= key[len(code1):-len(code2)]
                            mkey= Fernet(key1) 
                            userIdF = mkey.decrypt(info[1])
                            pseudoPasskeyF = mkey.decrypt(info[3])
                            if  userId == userIdF.decode() and Passkey == pseudoPasskeyF.decode():
                                key2= mkey.decrypt(info[4])
                                print("Welcome Back!, ", userId,"\n")
                                postKey = Fernet(key2)
                                return userId, postKey, fileCode
                except EOFError:
                    print("User ID or password is incorrect, Try again... \n\n\n")           
                    verify()

def view():
    '''{'checkFile': fileCode, 'check': userId, 'file': ['file1.txt', 'file2.txt']}    '''
    # Load passwords from file
    with open('password.bin', 'rb') as f:
        while True:
            try:
                data = pickle.load(f)
            except EOFError:
                break
            for item in data:
              #  print(postKey.decrypt(item['check'].decode()))
                if item['checkFile'] == fileCode:
                  #  print(fileCode, postKey.decrypt(item['check']))
                    data = item['file']
                    # Decrypt the data and print it in a tabular format
                    file = [list(map(postKey.decrypt, sublist)) for sublist in data]
                    print(file)
                    print("__|_________________|______________________|_______________|__")
                    print("  |account type     | username/E-mail      | password      |")
                    print("  |-----------------|----------------------|---------------|")
                    for row in file:
                        print("  | {:<16}| {:<20} | {:<14}|".format(*(x.decode() for x in row)))
                    print("__|_________________|______________________|_______________|__")
                    print("  |                 |                      |               |")
                    time.sleep(1)
                    break
            else:
                print("\n\nNo related data to load")
                   

def add():
    Macc=account = input("Enter account type: ")
    Muser=username = input("Enter username/E-mail address: ")
    Mpass= password= input("Enter password: ")
    print("New entry details are: \n Account: {} \n Username: {} \n Password: {} \n press (c) to confirm, (t) to try again and (q) to go to main menu".format(account, username, password))
    if input() == 'c':
        showEntry = [Macc, Muser, Mpass]
        print("__|_________________|______________________|_______________|__")
        print("  |account type     | username/E-mail      | password      |")
        print("  |-----------------|----------------------|---------------|")
        print("  | {:<16}| {:<20} | {:<14}|".format(*showEntry))
        print("__|_________________|______________________|_______________|__")
        print("  |                 |                      |               |")
        acc = postKey.encrypt(account.encode())
        user = postKey.encrypt(username.encode())
        passwd = postKey.encrypt(password.encode())
        Entry = [acc, user, passwd]
        with open ('password.bin', 'rb') as update:
            openF= pickle.load(update)
        while True:
            for item in openF:
                if item['checkFile'] == fileCode:
                    item['file'].append(Entry)
            break
        with open('password.bin', 'wb') as update:
            pickle.dump(openF, update)
        print("\n\nhey" , userId + "! \nEntry added successfully, to add another entry press (E) or press (q) to go to main menu")
        while True:
            if input().lower()== 'e':
                add()
            elif input().lower()=='q':
                print('redirecting to the main menu')
                time.sleep(2)
                os.system('clear')
                break
            else:
                print('incorrect key pressed, try again..')
                time.sleep(2)
                os.system('clear||cls')
                continue
                
    elif input() == 't':
        print("Try again...")
        time.sleep(1)
        return add()
    elif input().lower()== 'q':
                print('redirecting to the main menu')
                time.sleep(2)
                os.system('clear')
    else:
        print('incorrect key pressed, try again..')
        time.sleep(1)
        os.system('clear||cls')
        add() 