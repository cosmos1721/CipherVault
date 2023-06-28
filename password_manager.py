import os
import time
import definedFunc as df


# main program      
def exit_program():    
    print("Thank you for using the password manager")
    time.sleep(1)    
    print("Exiting...")
    exit()

def main():
    os.system('clear||cls')
    print("Welcome to the password manager")        
    user_login= input( 'Do you have an existing master key?  \n (q) for quit \n choose (y/n/q): ').lower()
    if user_login == 'q':
        exit_program()
    elif user_login=="y":
        if df.verify() == False:
            main()
        True
    elif user_login=="n": 
        df.newMasterKey()
        main()
    else:
        print("Invalid options, choose the correct one \n reloading...")
        time.sleep(1)
        main()

main()

while True:        
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit.: ")
    if mode == "q": exit_program()
    elif mode == "view":
        df.view()
    elif mode == "add":
        if df.add() == False:
            break
    else:
        print("Invalid mode")
    