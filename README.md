# Password-manager
The project provides a basic password manager functionality. It allows users to securely store and manage their passwords by encrypting and storing them locally on their machine. The program provides the following features:

1. Creation of a Master Key: Each user can create a new master key by providing a user ID and a master password. The master key is used for 
                             encrypting and decrypting the stored passwords.
2. Authentication: Users can authenticate themselves by entering their user ID and master password.
3. Viewing Passwords: Authenticated users can view their stored passwords in a tabular format. The passwords are decrypted using the master key along with a 
                      custom decryption technique.
4. Adding Passwords: Authenticated users can add new passwords to the password manager. The entered account details are encrypted using the master key and 
                     stored for future retrieval.

It can be experimented using the [link](https://replit.com/@cosmos1721/passwordmanager?v=1)

## Installation and usage
### Pre-requisites:
python/python3 to be installed on the computer. For installations, refer [python.org](https://www.python.org/downloads)

Open Terminal and use the following command:

    git clone https://www.github.com/cosmos1721/password_manager && cd password_manager
    python3 password_manager.py

## Conclusion
The overall aim is to provide users with a secure and convenient way to manage their passwords, allowing them to have unique and strong passwords for each account without the need to remember them all. The final expected product is to be run on a cloud server with better code-base and more functionalities to be available online with UI
