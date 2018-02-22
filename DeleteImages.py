import time
import os
from sys import argv
script_name = argv
choice=input("Do you want to validate each delete operation? ")
print("EXIT AT ANYTIME USING exit")

#asks before every delete

if(choice == "yes"):
    for i in os.listdir():
        if i.endswith(".jpg"):
            confirm=input("Do you want to delete "+i+" ?\n")
            if(confirm =="yes"):
                os.remove(i)
                print(i+" was successfully removed\n ")
            elif(confirm =="no"):
                print(i+" will not be deleted\n ")
            elif(confirm =="exit"):
                quit()

#Directly deletes all images

elif(choice == "no"):
    for i in os.listdir():
        if i.endswith(".jpg"):
            os.remove(i)
            print("\n"+i+" was successfully removed")
elif(choice == "exit"):
    quit()

count=0

#Mentions how many files remaining

for i in os.listdir():
    if i.endswith(".jpg"):
        count+=1
if(count == 0):
    print("No more files remaining!")
else:
    print(count,"images remaining in this folder")
time.sleep(5)
