#!/usr/bin/python3
# Kuznik Jakub
# xkuzni04@stud.fit.vutbr.cz

import math
import os.path                      ## For checking if file exist 
import time
import numpy as np
from numpy import mean              ## Expected value

import sys
from numpy.core.fromnumeric import shape, size
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
    print("     Command: basic      || 0 ......    ./iss.py input_file basic")
    print("     Command: frame      || 1 ......    ./iss.py input_file frame")
    print("     Command: dft        || 2 ......    ./iss.py input_file dft")
    print("     Command: spect      || 3 ......    ./iss.py input_file spect")
    print("     Command: dist       || 4 ......    ./iss.py input_file dist")
    print("     Command: gene       || 5 ......    ./iss.py input_file gene")
    print("     Command: gen_filt   || 6 ......    ./iss.py input_file gen_filt")
    print("     Command: nul_p      || 7 ......    ./iss.py input_file nul_p")
    print("     Command: freq       || 8 ......    ./iss.py input_file freq")
    print("     Command: filt       || 9 ......    ./iss.py input_file freq")
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
    
    inc = 512    # overlap by 512
    width = 1024 # one frame lenght    

    #new_data = np.copy(data)
    #new_data[0:len(data)] = 0
    
    new_data = []
    
    # Get information about signal
    data_min, data_max, lenght_sec, lenght_sam = basic_signal_info(data, sample_rate)

    for i in range(0, lenght_sam, inc):
        new_data += [data[i:i+width]]

    ## TODO PRINT AND CREATE PRINTING FUNCITON

    new_data = np.array(new_data)
    return new_data



##################### 
# Načtený signál ustředněte (odečtěte střednı́ hodnotu) a normalizujte do dynamického rozsahu -1 až 1 dělenı́m
# maximem absolutnı́ hodnoty. Signál rozdělte na úseky (rámce) o délce 1024 vzorků s překrytı́m 512 vzorků, rámce
# uložte jako sloupce matice. Vyberte ”pěkný” rámec s periodickým charakterem (znělý) a zobrazte jej se slušnou
# časovou osou v sekundách.
def com_2_frame(data, sample_rate):
    
    print("Frame")
    data = center_signal(data)
    data = normalize_signal(data)
    basic_signal_info_print(data, sample_rate)
    
    data = split_to_frames(data, sample_rate)
    data = data[1024:2048]

    # time from to 
    time = np.linspace(0, 1)
    plt.figure(figsize=(20,10))
    plt.plot(time, data, label="", color="green")
    plt.plot(time, data, label="")
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.savefig('out.pdf', bbox_inches="tight")
    plt.show()

    #create_picture(data, sample_rate)
    return 0



##################### 
# Implementujte vlastnı́ funkci pro výpočet diskrétnı́ Fourierovy transformace pro N=1024 vzorků. Snažte se pra-
# covat ”vektorově”, tedy s minimálnı́m počtem cyklů. Transformace by měla být realizována jako násobenı́ matice
# bázı́ s vektorem signálu. Spusťte Vaši funkci na vybraném rámci, zobrazte modul DFT pro frekvence od 0 do F 2 s
# se slušnou frekvenčnı́ osou v Hz. Porovnejte Váš výsledek s knihovnı́ implementacı́ FFT (např. np.fft.fft) -
# graficky a budete-li chtı́t, pomocı́ funkce na přibližné porovnánı́, např. np.allclose.
def com_2_dtf(data, sample_rate):
    print("DTF")
    return 0

##################### 
# Pro celý signál vypočtěte a zobrazte “logaritmický výkonový spektrogram” tedy obrázek s časem v sekundách
# na x-ové ose a s frekvencı́ v Hz na y-ové ose (opět do poloviny vzorkovacı́ frekvence). Použijte opět délku okna
# 1024 vzorků a překrytı́ 512 vzorků. Hodnoty jednotlivých koeficientů DFT upravte pomocı́ P [k] = 10 log 10 |X[k]| 2 .
# Můžete využı́t knihovnı́ funkci, ale rádi bychom, aby časová a frekvenčnı́ osa měly správné hodnoty. Pro hodnotu
# koeficientu můžete dle libosti použı́t stupeň šedi nebo barvu.
def com_3_spectogram(data, sample_rate):
    print("spectogram")
    return 0


##################### 
# Na spektrogramu budou jasně viditelné rušivé komponenty. Určete jejich frekvence f 1 , f 2 , f 3 , f 4 v Hz. Ověřte, že
# jsou 4 rušivé cosinusovky harmonicky vztažené, tedy že f 2 , f 3 a f 4 jsou násobky té nejnižšı́ frekvence. Na určenı́
# frekvencı́ si můžete napsat funkci nebo je odečı́st “ručně” ze spektrogramu či jednoho spektra.
# Hint: při odečı́tánı́ z jednoho spektra si dejte pozor na to, abyste rušivou frekvenci nezaměnili za součást
# spektra řeči.
def com_4_dist(data, sample_rate):
    print("dist")
    return 0


##################### 
# Generovánı́ signálu – 3 body
# Vygenerujte signál se směsı́ 4 cosinusovek na frekvencı́ch f 1 , f 2 , f 3 , f 4 , o stejné délce jako původnı́ signál. Uložte
# jej do souboru audio/4cos.wav. Zobrazte jeho spektrogram. Poslechem a srovnánı́m spektrogramů ověřte, že
# jste frekvence určili a signál vygenerovali správně.
def com_5_gene(data, sample_rate):
    print("generate")
    return 0


##################### 
# Čisticı́ filtr – 3 body
# Navrhněte filtr nebo sadu filtrů typu pásmová zádrž pro čištěnı́ signálu — musı́ potlačovat frekvence f 1 , f 2 , f 3 ,
# f 4 . Můžete postupovat jednou ze třı́ alternativ:
def com_6_gene_filt(data, sample_rate):
    print("clean")
    return 0


##################### 
# Nulové body a póly – 2 body
# Vypočtěte nulové body a póly navrženého filtru nebo filtrů a zobrazte je v komplexnı́ rovině. Zde budou ve
# výhodě uživatelé Matlabu či Octave, kteřı́ využijı́ funkce zplane. Pythonisté si ji budou muset naprogramovat
# (asi 5 řádků, využijte np.roots) nebo vygooglit již hotovou.
def com_7_nul_p(data, sample_rate):
    print("nul points ")
    return 0

##################### 
# Frekvenčnı́ charakteristika – 2 body
# Vypočtěte frekvenčnı́ charakteristiku filtru/filtrů a zobrazte ji/je se slušnou frekvenčnı́ osou v Hz. Ověřte, že filtr
# potlačuje rušivý signál na správných frekvencı́ch.
def com_8_freq(data, sample_rate):
    print("freq charac")
    return 0


##################### 
# Frekvenčnı́ charakteristika – 2 body
# Vypočtěte frekvenčnı́ charakteristiku filtru/filtrů a zobrazte ji/je se slušnou frekvenčnı́ osou v Hz. Ověřte, že filtr
# potlačuje rušivý signál na správných frekvencı́ch.
def com_9_filt(data, sample_rate):
    print("filter ")
    return 0


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
        com_2_dtf(data, sample_rate)
    elif command == "spect" or command == "3":
        com_3_spectogram(data, sample_rate)
    elif command == "dist" or command == "4":
        com_4_dist(data,sample_rate)
    elif command == "gene" or command == "5":
        com_5_gene(data,sample_rate)
    elif command == "gen_filt" or command == "6":
        com_6_gene_filt(data,sample_rate)
    elif command == "nul_p" or command == "7":
        com_7_nul_p(data,sample_rate)
    elif command == "freq" or command == "8":
        com_8_freq(data,sample_rate)
    elif command == "filt" or command == "9":
        com_9_filt(data,sample_rate)
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
