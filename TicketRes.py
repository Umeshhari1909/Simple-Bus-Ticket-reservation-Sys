from random import randint
from datetime import datetime
import os
import keyboard
import sys

class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination,No_Tickets):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.No_Tickets=No_Tickets
        Ticket.counter+=No_Tickets
        
    def generate_ticket(self):
        if (Ticket.counter>50):
            print("Sorry to inform you that we are Short of {} tickets" .format(Ticket.counter-50))

        else:
            __ticket_id=self.__source[0]+self.__destination[0]+"0"+str(randint(0,100))
            print("Name of Recipient : {}".format(self.__passenger_name))
            print( "Ticket id will be:",__ticket_id)
            print("No of Tickets :",self.No_Tickets)
            print("Source :{}".format(self.__source))
            print("Destination :{}".format(self.__destination))
            print("Booking Time and Date :{}".format(datetime.now()))

def Booking():
    print("\n\nWelcome! To Ticket Booking System\n")
    Name=input("Enter your Name :")
    Source=input("Enter the Source :")
    Destination=input("Enter the Destination :")
    Number= int(input("Enter the number of Tickets :"))
    T1=Ticket(Name,Source,Destination,Number)
    T1.generate_ticket()
Booking()
print("Press Y to continue Booking...")
print("Press N to exit")
while True:
    if keyboard.is_pressed('y'):
        Booking()
    elif keyboard.is_pressed('n') :
        sys.exit(0)
        
        
        

