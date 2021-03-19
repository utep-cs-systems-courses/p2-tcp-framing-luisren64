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

        #args = myReadline()


def myReadline():
    #code here
        
