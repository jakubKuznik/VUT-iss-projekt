#!/usr/bin/python3
# Kuznik Jakub
# xkuzni04@stud.fit.vutbr.cz


import os.path
import time
import numpy as np
import sys
from scipy.io import wavfile ## For waw file loading

##
# Prints help message
def help():
    print("execution: ..........    ./iss.py input_file [command]")
    print("execution: ..........    ./iss.py -h")
    print(".......................................................")
    print("     Command: frame ......    ./iss.py input_file frame")
    print("     Command: dft   ......    ./iss.py input_file dft")
    print("     Command: spect ......    ./iss.py input_file spect")
    print("     Command: dist  ......    ./iss.py input_file dist")
    print("     Command: gene  ......    ./iss.py input_file gene")
    print("     Command: nul_p ......    ./iss.py input_file nul_p")
    print("     Command: filt  ......    ./iss.py input_file filt")
    print("     Command: freq  ......    ./iss.py input_file freq")
    print("......................................................")
    return 0


##
# Parse arguments that are stored in args
# If error or -help exit() program
# return file_path, command
def parse_arguments(args):
    
    file_path   = ""    # Store path to input file 
    command     = ""    # Command 

    if len(args) == 1:      # If there are no arguments.
        print("ERROR BAD ARGUMENTS")
        print("try:")
        help()
        exit()
    elif len(args) == 2:    # If there is just one argument. 
        file_path = args[1]
    else:                   # store file_path and program. 
        file_path = args[1]
        command = args[2]

    # if help print them exit program 
    if args[1] == "-h" or args[1] == "--help" or args[1] == "-help":
        help()
        exit()

    return file_path, command


##
#
def open_waw_file():
    
    return 0

##
#
def main():

    file_path = ""  # Path to waw file.
    command = ""    # Command that will be executed.

    file_path, command = parse_arguments(sys.argv)

    print(file_path, command)

    """

    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(array)
    """



if __name__ == '__main__':
    start = time.time()
    main()
    #print(time.time() - start)
