import random
import string
import datetime
import time
import userlogin

user = userlogin.account()

if(user):
    print("Welcome",user)
else:
    print("Not registered, please register")


#                  ARRIVAL TIME TIMER

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        print(timeformat, end='\r')
    print('Your ride has arrived!\n\n')
    print('Please submit',random.randint(1000,9999),'as the OTP')

#                  BOOKING CONFIRMATION
def booking():
    regno = [state_regno,random.randrange(0,51),state_regno,random.randint(1000,10000)]
    regno = (' '.join(str(e) for e in regno))
    print("Taxi number:",regno,"\nTime of booking: %s:%s " %(timee.hour,timee.minute),"\nDate: %s %s %s" %(date.day,date.month,date.year))
    confirm = input("\nConfirm booking?\n")
    print("Please wait, your ride is on the way!")
    countdown(5)


#                   INPUT DETAILS

name = user
print("Hello %s! Where do you want to go to?" %(user))
location = input()
record = name+"/"+location

#                   ADD DETAILS TO FILE

file = open("TAXILOG.txt","a")
file.write(record+"\n")
file.close()


choice = input("Do you want to pool a ride on the way to "+location+"?\n")
poolers = []

#                   BOOKING/TAXI DETAILS

state_regno= random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)
timee=datetime.datetime.now().time()
date=datetime.datetime.now().date()

if( choice == "yes" or  choice == "y"):
    print("Looking for a Co-passenger")


#                   RANDOM DELAY GIMMICK
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")

#               SEARCH FILE FOR POOLING MATCHES
    file = open("TAXILOG.txt","r")
    for line in file:
#               FIND SEPERATOR
        index=line.find("/")
#               VALIDATE MATCH
        if(location == line[index+1:].strip() and name != line[:index] ):
            poolers.append(line[:index])
    if(poolers):
        print("You'll be pooling with "+','.join(poolers))
        booking()
    else:
        print("\nNo poolers, enjoy your solo adventure!")
        booking()

else:
    print("You're riding solo\n")
    booking()
