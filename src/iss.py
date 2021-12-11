#!/usr/bin/python3
# Kuznik Jakub
# xkuzni04@stud.fit.vutbr.cz


import os.path                  ## for checking if file exist 
import time
import numpy as np
import sys
import wavio ## For waw file loading


##
# Prints help message
def help():
    print("execution: ..........    ./iss.py input_file [command]")
    print("execution: ..........    ./iss.py -h")
    print(".......................................................")
    print("     Command: frame || 1 ......    ./iss.py input_file frame")
    print("     Command: dft   || 2 ......    ./iss.py input_file dft")
    print("     Command: spect || 3 ......    ./iss.py input_file spect")
    print("     Command: dist  || 4 ......    ./iss.py input_file dist")
    print("     Command: gene  || 5 ......    ./iss.py input_file gene")
    print("     Command: nul_p || 6 ......    ./iss.py input_file nul_p")
    print("     Command: filt  || 7 ......    ./iss.py input_file filt")
    print("     Command: freq  || 8 ......    ./iss.py input_file freq")
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
# open file from filepath
def open_waw_file(filepath):

    ## if file doesn't exist.
    if os.path.isfile(filepath) == False:
        print("ERROR: file: .... " + filepath + " .... doesn't exist.")
        exit()

    ## Open waw file
    # Code from iss_project: Zmolikova #####################
    d = wavio.read(filepath)
    data = d.data
    data = data / 2 ** 15   ## NORMALIZE SIGNAL MAGIC CONSTANT
    print(data.min(), data.max())
    ########################################################
    return 0

##
# Call command exit program if error.  
def call_command(command, data):
    
    if len(command) == 0:
        print("ERROR missing command.")
        exit(1)

    if command == "frame" or command == "1":
        print("frame")
    elif command == "dft" or command == "2":
        print("dft")
    elif command == "spect" or command == "3":
        print("spect")
    elif command == "dist" or command == "4":
        print("dist")
    elif command == "gene" or command == "5":
        print("gene")
    elif command == "nul_p" or command == "6":
        print("nul_p")
    elif command == "filt" or command == "7":
        print("filt")
    elif command == "freq" or command == "8":
        print("freq")
    else:
        print("ERROR unknow... " + command + " ...command.")
        exit(1)
    return 0

##
#
def main():

    file_path = ""  # Path to waw file.
    command = ""    # Command that will be executed.
    data = 0        # Data from waw file 


    file_path, command = parse_arguments(sys.argv) # get file_path and command 
    
    data = open_waw_file(file_path)                # open waw input file and store data 

    call_command(command, data)                    # Call propriate command

    """

    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(array)
    """



if __name__ == '__main__':
    start = time.time()
    main()
    #print(time.time() - start)
