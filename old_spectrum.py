#DR FOUCHE
#FCHDYL001
#UCT CS2

"""
    FFT Spectral Analysis
    This script uses a discrete fourier transform to perform a spectral analysis on an audio file, and matplotlib to graph the frequency response.
    
    @author dylanfouche@gmail.com
    @version 1.1
    @param filename, pointer to a 32-bit 44.1kHz .wav file
    @param filename1, optional, pointer to a second 32-bit 44.1kHz .wav file
"""

import scipy.io.wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
import sys

CHUNK = 44100*3
RATE = 44100	

def main():

    if (len(sys.argv)==2):
    
        filename = sys.argv[1]	
        samplerate, data = scipy.io.wavfile.read(filename)
        assert(samplerate==RATE)
    
        fourier = np.abs(fft(data))[0:CHUNK]
        xf = np.linspace(0,RATE,CHUNK)    		
        yf = np.interp(fourier, (fourier.min(),fourier.max()), (0,1))

        plt.plot(xf,yf)
        plt.xlim(20,RATE/2)
        plt.xscale('log')
        plt.title("Spectral Analysis of " + filename)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.show()
    
    elif (len(sys.argv)==3):
        
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]	
        samplerate1, data1 = scipy.io.wavfile.read(filename1)
        samplerate2, data2 = scipy.io.wavfile.read(filename2)
        assert(samplerate1==RATE and samplerate2==RATE)
    
        fourier1 = np.abs(fft(data1))[0:CHUNK]
        fourier2 = np.abs(fft(data2))[0:CHUNK]
        xf = np.linspace(0,RATE,CHUNK)    		
        yf1 = np.interp(fourier1, (fourier1.min(),fourier1.max()), (0,1))
        yf2 = np.interp(fourier2, (fourier2.min(),fourier2.max()), (0,1))

        plt.plot(xf,yf1)
        plt.plot(xf,yf2)
        plt.legend([filename1, filename2])
        plt.xlim(20,RATE/2)
        plt.xscale('log')
        plt.title("Spectral Analysis of " + filename1 + " vs " + filename2)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.show()

if __name__ == "__main__":
    main()