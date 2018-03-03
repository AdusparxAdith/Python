import os
import resources
import getpass

def account():
    choice = input("1. Existing user\n2. Register new user\n")
#                       EXISTING USER
    if ( choice == "1"):
        os.system("cls")

        resources.line()
        print("\nLOGIN\n")
        resources.line()

        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        file = open("userdatabase.txt","r")

        for line in file:
            index = line.find("/")
            if(line[:index].strip() != username and line[index+1:].strip() != password):
                continue
            else:
                return(username)
        return(None)

#                       REGISTER NEW USER
    elif ( choice == "2"):
        os.system("cls")

        resources.line()
        print("\nREGISTER\n")
        resources.line()

        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        file = open("userdatabase.txt","a")
        file.write(username+"/"+password+"\n")
        return(username)
