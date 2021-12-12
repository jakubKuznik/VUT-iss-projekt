#!/usr/bin/python3
# Kuznik Jakub
# xkuzni04@stud.fit.vutbr.cz

import math
import os.path                      ## For checking if file exist 
import time
import numpy as np
from numpy import mean              ## Expected value

import sys
import wavio                        ## For waw file loading
import matplotlib.pyplot as plt     ## For signal pictures
import matplotlib.colors as mcolors ## For signal plot collor 

from scipy.io import wavfile

##
# Prints help message
def help():
    print("execution: ..........    ./iss.py input_file [command]")
    print("execution: ..........    ./iss.py -h")
    print(".......................................................")
    print("     Command: basic || 0 ......    ./iss.py input_file basic")
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
# Get basic info about signal.
# Maximum and minimum value.
# Lenght in sec and samples.
def basic_signal_info(data, sample_rate):

    data_min = data.min()
    data_max = data.max()
    lenght_sec = (data.shape[0] / sample_rate)
    lenght_sam = data.shape[0]

    return data_min, data_max, lenght_sec, lenght_sam

##
# print basic info about signals same as basic_signal_info
# Maximum and minimum value
# lengt in sec and samples 
def basic_signal_info_print(data, sample_rate):
    print("data min:            ", data.min() )
    print("data max:            ", data.max() )
    print("samples:             ", sample_rate)
    print("lenght in sec:       ", (data.shape[0] / sample_rate))
    print("lenght in samples:   ", data.shape[0] )


##
# Create picture and store to out.pdf  
def create_picture(data, sample_rate):

    # Get information about signal
    data_min, data_max, lenght_sec, lenght_sam = basic_signal_info(data, sample_rate)

    # time from to 
    time = np.linspace(0, lenght_sec, lenght_sam)
    plt.figure(figsize=(20,10))
    plt.plot(time, data, label="", color="green")
    plt.plot(time, data, label="")
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.savefig('out.pdf', bbox_inches="tight")
    plt.show()

##
# open file from filepath
def open_waw_file(filepath):

    ## if file doesn't exist.
    if os.path.isfile(filepath) == False:
        print("ERROR: file: .... " + filepath + " .... doesn't exist.")
        exit()

    ## Open waw file
    # Code from iss_project: Zmolikova #####################
    sample_rate, data = wavfile.read(filepath)
    ########################################################
    return sample_rate, data

##
# Central signal by sub Epected value (střední hodnota)
def center_signal(data):
    expected_value = mean(data)
    data = data - expected_value
    return data

##
# Normalize data 
def normalize_signal(data):
    data_abs = abs(data)
    max_value = max(data_abs)
    return (data / max_value) 


##
# Split signal to frames with 1024 samples each frame overlaps frame before by 512
def split_to_frames(data, sample_rate):
    
    # Get information about signal
    data_min, data_max, lenght_sec, lenght_sam = basic_signal_info(data, sample_rate)

    frames_sum = math.ceil(lenght_sam/1024)      #math.ceil number round up

    for i in range(0, frames_sum):
        for j in range(0, 1023):
            print(data[j])
    
    return 0

##################### 
# Načtený signál ustředněte (odečtěte střednı́ hodnotu) a normalizujte do dynamického rozsahu -1 až 1 dělenı́m
# maximem absolutnı́ hodnoty. Signál rozdělte na úseky (rámce) o délce 1024 vzorků s překrytı́m 512 vzorků, rámce
# uložte jako sloupce matice. Vyberte ”pěkný” rámec s periodickým charakterem (znělý) a zobrazte jej se slušnou
# časovou osou v sekundách.
def com_2_frame(data, sample_rate):
    
    print("frame")
    data = center_signal(data)
    data = normalize_signal(data)
    basic_signal_info_print(data, sample_rate)
    
    #data = split_to_frames(data, sample_rate)
    split_to_frames(data, sample_rate)

    create_picture(data, sample_rate)



##
# Call command exit program if error.  
def call_command(command, data, sample_rate):


    if len(command) == 0:
        print("ERROR missing command.")
        exit(1)
    
    ## normalize signal for commands 1 - 8
    #if command != "basic" and command != "0":
    #    data = normalize_signal(data)


    if command == "basic" or command == "0":
        create_picture(data, sample_rate)
    elif command == "frame" or command == "1":
        com_2_frame(data, sample_rate)
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

    file_path = ""      # Path to waw file.
    command = ""        # Command that will be executed.
    data = 0            # Data from waw file 
    sample_rate = 0     # sample rate of waw file 
    


    file_path, command = parse_arguments(sys.argv)  # get file_path and command 
    
    sample_rate, data = open_waw_file(file_path)    # open waw input file and store data 

    basic_signal_info_print(data, sample_rate)      # Print basic info about signal 

    call_command(command, data, sample_rate)        # Call propriate command


if __name__ == '__main__':
    start = time.time()
    main()
    #print(time.time() - start)