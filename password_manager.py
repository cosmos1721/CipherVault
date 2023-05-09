import os
import time
import definedFunc as df


# main program      
def exiter():    
    print("Thank you for using the password manager")
    time.sleep(1)    
    print("Exiting...")
    exit()

while  True:
    os.system('clear||cls')
    print("Welcome to the password manager")        
    user_login= input( 'Do you have an existing master key?  \n (q) for quit \n choose (y/n/q): ').lower()
    if user_login == 'q':
        exiter()
    elif user_login=="y":
        df.verify()
        break
    elif user_login=="n": 
        df.newMasterKey()
    else:
        print("Invalid options, choose the correct one \n reloading...")
        time.sleep(2)

while True:        
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit.\t")
    if mode == "q": exiter()
    elif mode == "view":
        df.view()
    elif mode == "add":
        df.add()
    else:
        print("Invalid mode")
    