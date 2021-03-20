#! /usr/binenv/python3
import os
import sys
import re

def main():

    #Here we will accept input to transfer
    while True:
        if 'PS1' in os.environ:
            os.write(2, (os.environ['PS1'}).encode())
        else:
            os.write(2, "$".encode())

        args = myReadline().split(" ") #Seperating into different words"

        if args[0] == "exit" or if args[0] == "Exit":
            os.write(2, "Exiting \n".encode())
            sys.exit(0)


#Method to read the input that will be sent as a message
def myReadline():
    #code here
    i = 0
    inp = "" 
    inbuff = read(0,100) #Making a buffer to read the input message to be sent.
    temp = inbuff.decode()

    while i < len(inp):
        curr = temp[i] #temp variable for each char in the input string

        #As long as we do not reach the newline, we keep adding chars
        if curr != '\n':
            inp += curr
            i = i+1

        #We've reached the newline, return inp
        else:
            print(inp) #TEST DELETE LATER
            return inp

    return ""
        
