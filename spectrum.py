#    D FOUCHE
#    UCT CS3
#    FCHDYl001


import scipy.io.wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
import sys

CHUNK = 44100*3
RATE = 44100

def main():
    #read in audio file
    filename = sys.argv[1]
    samplerate, data = scipy.io.wavfile.read(filename)
    assert(samplerate==RATE)
    #perform fft
    fourier = np.abs(fft(data))[0:CHUNK]
    xf = np.linspace(0,RATE,CHUNK)
    yf = np.interp(fourier, (fourier.min(),fourier.max()), (0,1))
    #display spectrum
    plt.plot(xf,yf)
    plt.xlim(20,RATE/2)
    plt.xscale('log')
    plt.title("Spectral Analysis of " + filename)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.show()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
		quit()
	except:
		print("Some other error occurred")
		print(e.message)
		quit()
