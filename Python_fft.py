from scipy.fftpack import fft
from scipy.signal import welch
import numpy as np
##initilizing Number of smaple points
N=1000
#Sample spacing
T=1.0/500.0
fs=1/T

x=np.linspace(0.0,N*T,N)
y=np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)+0.5*np.sin(20.0 * 2.0*np.pi*x)
def get_fft_psd(y,T,N,fs):
    yft=fft(y)
    xpd,ypd=welch(y,fs)
    xft=np.linspace(0.0,1.0/(2.0*T),N//2)

    return xft,yft,xpd,ypd
xft,yft,xpd,ypd = get_fft_psd(y,T,N,fs)
import matplotlib.pyplot as plt
plt.plot(xft,2.0/N*np.abs(yft[0:N//2]),color='blue')
plt.grid()
plt.plot(xpd,ypd,color='orange')
plt.grid()
plt.show()


#############################

