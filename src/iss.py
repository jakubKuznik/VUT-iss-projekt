#!/usr/bin/python3
# Kuznik Jakub
# xkuzni04@stud.fit.vutbr.cz

import math
import os.path                      ## For checking if file exist 
import time
import numpy as np
import cmath    
from numpy import mean              ## Expected value

import sys
import numpy
from numpy.__config__ import show
from numpy.core.fromnumeric import shape, size
import wavio                        ## For waw file loading
import matplotlib.pyplot as plt     ## For signal pictures
import matplotlib.colors as mcolors ## For signal plot collor 

import scipy.io as sc
from scipy.io import wavfile
from scipy.signal import spectrogram, lfilter, freqz, tf2zpk
from scipy.io.wavfile import write


from IPython.display import Audio


##
# Prints help message
def help():
    print("execution: ..........    ./iss.py input_file [command]")
    print("execution: ..........    ./iss.py -h")
    print(".......................................................")
    print("     Command: basic      || 0 ......    ./iss.py input_file basic")
    print("     Command: frame 0    || 1 ......    ./iss.py input_file frame")
    print("     Command: dft        || 2 ......    ./iss.py input_file dft")
    print("     Command: spect      || 3 ......    ./iss.py input_file spect")
    print("     Command: gen_filt   || 5 ......    ./iss.py input_file gen_filt")
    print("     Command: dist       || 4 ......    ./iss.py input_file dist   #generate cosin signal" )
    print("     Command: nul_p      || 6 ......    ./iss.py input_file nul_p")
    print("     Command: freq       || 7 ......    ./iss.py input_file freq")
    print("     Command: filt       || 8 ......    ./iss.py input_file freq")
    print("......................................................")
    return 0


frame = 10


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
    a, b, lenght_sec, lenght_sam = basic_signal_info(data, sample_rate)

    # time from to
    time = np.linspace(0, lenght_sec, lenght_sam)
    plt.figure(figsize=(20,10))
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
    a, b, c, lenght_sam = basic_signal_info(data, sample_rate)
    
    inc = 512    # overlap by 512
    width = 1024 # one frame lenght        
    new_data = []
    

    for i in range(0, lenght_sam, inc):
        new_data += [data[i:i+width]]


    new_data = np.array(new_data) ## transpon matrix
    return new_data 

##
# 0 frame is from 0 - 1024 
# 1 frame is from 512 - 1536 
# reurn frame time from to 
def get_frame_info(frame_size, frame_index, lenght_sec, lenght_sam):

    one_sample_time = lenght_sec / lenght_sam
    time_from = (frame_index*512)*one_sample_time
    time_to = time_from + (frame_size*one_sample_time) 

    return one_sample_time, time_from, time_to

##
# Plt one frame
# lengt_sec, lenght_sam - are lenght of whole datas 
def plt_frame(data, frame_width, x_from, x_to, x_label, y_label):

    time = np.linspace(x_from, x_to, frame_width) 
    plt.figure(figsize=(20,10))
    plt.plot(time, data, label="")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig('out.pdf', bbox_inches="tight")
    plt.show()

##
# Create cosinus
#   amplitude     - cos amplitudu - signal height 
#   freq          - frequency of cosin in hz 
#   sample_rate   - sample rate 16 000
#   sample_lenght - lenght of singal in samples
def generate_cosinus(amplitude, freq, sample_rate, sample_lenght):
    t = np.arange(sample_lenght) # generate matrix 
    return (amplitude * np.cos(2 * (np.pi)/sample_rate * freq * t))

##
# Plot spectogram 
def plot_spectogram(data, sample_rate, frame_width, noverlap):
    plt.figure(figsize=(20,10))
    plt.specgram(data, Fs=sample_rate, NFFT=frame_width, noverlap=noverlap, mode='psd', scale='dB')
    plt.ylabel('Frekvence [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar()
    plt.savefig('out.pdf', bbox_inches="tight")
    plt.show()


##
# Realise DFT.
def dtf_func(data, index):
    
    one_frame = data[index]

    N = len(one_frame)                       # Samples in data 
    n = np.arange(N)                         # create values from 0 1 2 ... 1024[frame_width]
    k = n.reshape((N, 1))                    # 1d array of size N in y-axis
    M = np.exp(-2j * np.pi * k * n / N)      # 2d array(matrix) of size N**2
    fourier = np.dot(M, one_frame)           # multiply 1d data matrix with 2d
    half = math.ceil(N/2)
    return np.abs(fourier[0:half])             # resize to half becouse second half is same

### SAME BUT SLOW 
#    for i in range(0,len(data)-1):
#        fourier.append(dtf_func(data, i))
#        matrix[0:512,i] = fourier[i]
#
#    ##### TODO rework to matrix 
#    N = len(data[index]) ## number of samples
#    for k in range(N): 
#        a = 0
#        for n in range(N):
#            a += one_frame[n]*cmath.exp(-2j * cmath.pi * k * n * (1/N))
#        if k == 512: break
#        fourier[0].append(a)
#    ###################################################################
#    fourier[0] = np.abs(fourier[0])
#    return fourier[0]
#


##################### 
# Načtený signál ustředněte (odečtěte střednı́ hodnotu) a normalizujte do dynamického rozsahu -1 až 1 dělenı́m
# maximem absolutnı́ hodnoty. Signál rozdělte na úseky (rámce) o délce 1024 vzorků s překrytı́m 512 vzorků, rámce
# uložte jako sloupce matice. Vyberte ”pěkný” rámec s periodickým charakterem (znělý) a zobrazte jej se slušnou
# časovou osou v sekundách.
def com_1_frame(data, sample_rate):
    
    print("Frame")
    
    frame_width = 1024 ## width of one frame 
    a, b, lenght_sec, lenght_sam = basic_signal_info(data, sample_rate)

    ## normalize center and split to frames 
    data = center_signal(data)
    data = normalize_signal(data)
    data = split_to_frames(data, sample_rate)   


    ## GET INFO ABOUT FRAME 
    step, time_from, time_to = get_frame_info(frame_width, frame, lenght_sec, lenght_sam) 

    print(time_to-time_from)

    plt_frame(data[frame], frame_width, time_from, time_to ,"time [s]", "Amplitude")





##################### 
# Implementujte vlastnı́ funkci pro výpočet diskrétnı́ Fourierovy transformace pro N=1024 vzorků. Snažte se pra-
# covat ”vektorově”, tedy s minimálnı́m počtem cyklů. Transformace by měla být realizována jako násobenı́ matice
# bázı́ s vektorem signálu. Spusťte Vaši funkci na vybraném rámci, zobrazte modul DFT pro frekvence od 0 do F 2 s
# se slušnou frekvenčnı́ osou v Hz. Porovnejte Váš výsledek s knihovnı́ implementacı́ FFT (např. np.fft.fft) -
# graficky a budete-li chtı́t, pomocı́ funkce na přibližné porovnánı́, např. np.allclose.
def com_2_dtf(data, sample_rate):
    print("DTF")
    
    frame_width = 1024 ## width of one frame 

    ## normalize center and split to frames 
    data = center_signal(data)
    data = normalize_signal(data)
    data = split_to_frames(data, sample_rate)   

    #fourier = []
    #fourier.append(dtf_func(data, frame))
    fourier = np.zeros((512,), dtype='complex_')
    fourier = dtf_func(data, frame)

    # plot fourier transform of one frame 
    plt_frame(fourier, frame_width/2, 0, frame_width/2 ,"FS [hz]", "Amplitude")
    
    

##################### 
# Pro celý signál vypočtěte a zobrazte “logaritmický výkonový spektrogram” tedy obrázek s časem v sekundách
# na x-ové ose a s frekvencı́ v Hz na y-ové ose (opět do poloviny vzorkovacı́ frekvence). Použijte opět délku okna
# 1024 vzorků a překrytı́ 512 vzorků. Hodnoty jednotlivých koeficientů DFT upravte pomocı́ P [k] = 10 log 10 |X[k]| 2 .
# Můžete využı́t knihovnı́ funkci, ale rádi bychom, aby časová a frekvenčnı́ osa měly správné hodnoty. Pro hodnotu
# koeficientu můžete dle libosti použı́t stupeň šedi nebo barvu.
def com_3_spectogram(data, sample_rate):
    
    print("spectogram")
    frame_width = 1024 ## width of one frame 
    noverlap = 512

    ## normalize center and split to frames 
    data = center_signal(data)
    data = normalize_signal(data)

    plot_spectogram(data, sample_rate, frame_width, noverlap)
   
    
    """
    MATICE
    
    data = split_to_frames(data, sample_rate)   

    print(len(data))
    # GET All spectra        matrix[0:512,i] = fourier[i]

    fourier = []
    matrix = np.zeros((512,63))
    print(len(data))

    for i in range(0,len(data)-1):
        fourier.append(dtf_func(data, i))
        matrix[0:512,i] = fourier[i]
        matrix[0:512,i] = 10 * np.log10((matrix[0:512,i])**2)

    f, t, sgr = spectrogram(sample_rate, matrix)
    """


##################### 
# Na spektrogramu budou jasně viditelné rušivé komponenty. Určete jejich frekvence f 1 , f 2 , f 3 , f 4 v Hz. Ověřte, že
# jsou 4 rušivé cosinusovky harmonicky vztažené, tedy že f 2 , f 3 a f 4 jsou násobky té nejnižšı́ frekvence. Na určenı́
# frekvencı́ si můžete napsat funkci nebo je odečı́st “ručně” ze spektrogramu či jednoho spektra.
# Hint: při odečı́tánı́ z jednoho spektra si dejte pozor na to, abyste rušivou frekvenci nezaměnili za součást
# spektra řeči.
##################### 
# Generovánı́ signálu – 3 body
# Vygenerujte signál se směsı́ 4 cosinusovek na frekvencı́ch f 1 , f 2 , f 3 , f 4 , o stejné délce jako původnı́ signál. Uložte
# jej do souboru audio/4cos.wav. Zobrazte jeho spektrogram. Poslechem a srovnánı́m spektrogramů ověřte, že
# jste frekvence určili a signál vygenerovali správně.
def com_4_dist(data, sample_rate):
    print("Generate signal from cosinus.")

    a, b, c, lenght_sam = basic_signal_info(data, sample_rate)
    
    # this freq i find in my spectogram. 
    # f2 is f1*2      f3 is f1*3    etc...
    # frequencies in [Hz]
    f1 = 720 
    frame_width = 1024 ## width of one frame 
    noverlap = 512     # frame overlaps 
    amplitude = 0.5    # apmpitude of cosine 

    # first cosinus for inicialization 
    cos = generate_cosinus(amplitude, f1, sample_rate, lenght_sam)
    for i in range(2,5): ## generate others cosinus.
        cos = cos + generate_cosinus(amplitude, i*f1, sample_rate, lenght_sam)

    plot_spectogram(cos, sample_rate, frame_width, noverlap) 

    Audio(data=cos, rate=sample_rate)
    ## store signal as .wav file 
    write("../audio/4cos.wav", sample_rate, cos)


##################### 
# Čisticı́ filtr – 3 body
# Navrhněte filtr nebo sadu filtrů typu pásmová zádrž pro čištěnı́ signálu — musı́ potlačovat frekvence f 1 , f 2 , f 3 ,
# f 4 . Můžete postupovat jednou ze třı́ alternativ:
def com_5_gene_filt(data, sample_rate):
    print("clean")


##################### 
# Nulové body a póly – 2 body
# Vypočtěte nulové body a póly navrženého filtru nebo filtrů a zobrazte je v komplexnı́ rovině. Zde budou ve
# výhodě uživatelé Matlabu či Octave, kteřı́ využijı́ funkce zplane. Pythonisté si ji budou muset naprogramovat
# (asi 5 řádků, využijte np.roots) nebo vygooglit již hotovou.
def com_6_nul_p(data, sample_rate):
    print("nul points ")

##################### 
# Frekvenčnı́ charakteristika – 2 body
# Vypočtěte frekvenčnı́ charakteristiku filtru/filtrů a zobrazte ji/je se slušnou frekvenčnı́ osou v Hz. Ověřte, že filtr
# potlačuje rušivý signál na správných frekvencı́ch.
def com_7_freq(data, sample_rate):
    print("freq charac")


##################### 
# Frekvenčnı́ charakteristika – 2 body
# Vypočtěte frekvenčnı́ charakteristiku filtru/filtrů a zobrazte ji/je se slušnou frekvenčnı́ osou v Hz. Ověřte, že filtr
# potlačuje rušivý signál na správných frekvencı́ch.
def com_8_filt(data, sample_rate):
    print("filter ")


##
# Call command exit program if error.  
def call_command(command, data, sample_rate):

    if len(command) == 0:
        print("ERROR missing command.")
        exit(1)

    if command == "basic" or command == "0":
        create_picture(data, sample_rate)
    elif command == "frame" or command == "1":
        com_1_frame(data, sample_rate)
    elif command == "dft" or command == "2":
        com_2_dtf(data, sample_rate)
    elif command == "spect" or command == "3":
        com_3_spectogram(data, sample_rate)
    elif command == "dist" or command == "4":
        com_4_dist(data,sample_rate)
    elif command == "gen_filt" or command == "5":
        com_5_gene_filt(data,sample_rate)
    elif command == "nul_p" or command == "6":
        com_6_nul_p(data,sample_rate)
    elif command == "freq" or command == "7":
        com_7_freq(data,sample_rate)
    elif command == "filt" or command == "8":
        com_8_filt(data,sample_rate)
    else:
        print("ERROR unknow... " + command + " ...command.")
        exit(1)


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
