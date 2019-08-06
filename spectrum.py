'''
    D FOUCHE
    UCT CS3
    FCHDYl001
'''

import scipy.io.wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
import sys
import traceback

CHUNK = 44100*3
RATE = 44100

def main():
    #read in audio file
    filename1 = sys.argv[1]
    samplerate1, data1 = scipy.io.wavfile.read(filename1)
    assert(samplerate1==RATE)
    #perform fft
    fourier1 = np.abs(fft(data1))[0:CHUNK]
    xf = np.linspace(0,RATE,CHUNK)
    yf1 = np.interp(fourier1, (fourier1.min(),fourier1.max()), (0,1))
    #display spectrum
    plt.plot(xf,yf1)
    plt.xlim(20,RATE/2)
    plt.xscale('log')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    if(len(sys.argv)==3):   #plot second spectrum
        #read in audio file
        filename2 = sys.argv[2]
        samplerate2, data2 = scipy.io.wavfile.read(filename2)
        assert(samplerate2==RATE)
        #perform fft
        fourier2 = np.abs(fft(data2))[0:CHUNK]
        yf2 = np.interp(fourier2, (fourier2.min(),fourier2.max()), (0,1))
        #display spectrum
        plt.plot(xf,yf2)
        plt.legend([filename1, filename2])
        plt.title("Spectral Analysis of " + filename1 + " vs " + filename2)
    else:
        plt.title("Spectral Analysis of " + filename1)

    plt.show()


if __name__ == "__main__":
    if not len(sys.argv) in {2,3}:
        print("Usage:\t $python3 spectrum.py [filename1] <filename2>")
        quit()
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        quit()
    except Exception as e:
        print("Some other error occurred:")
        print(traceback.print_exc())
        quit()
