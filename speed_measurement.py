from FFT import fft, plt, np
from scipy.io import wavfile
from doppler import v_receiver

'''
By Shao-Hsuan (Ernie) Chu, NSYSU, Taiwan
Default record file name: record.wav
Default source file name: 244hz.wav
'''

recordFile = input('Record file: ')
sourceFile = input('Souce file: ')

sample_rate, timeDomain = wavfile.read(recordFile)
plt.subplot(221)
plt.plot(range(len(timeDomain)), timeDomain)
plt.xlabel('(s)')
plt.title('Original wave with v')
freqDomain = fft(timeDomain)
freqData = abs(freqDomain)/len(freqDomain)
freqData = freqData[range(3000)]

fileLength = len(freqDomain)/sample_rate

x=np.linspace(0, 3000/fileLength, 3000)
plt.subplot(222)
plt.plot(x, freqData)
plt.xlabel('(Hz)')
plt.title('FFT of the wave(part)')

sample_rate_single, timeDomain_single = wavfile.read(sourceFile)
plt.subplot(223)
plt.plot(range(len(timeDomain_single)), timeDomain_single, 'g')
plt.xlabel('(s)')
plt.title('Original wave of single frequency')
freqDomain_single = fft(timeDomain_single)
freqData_single = abs(freqDomain_single)/len(freqDomain_single)
freqData_single = freqData_single[range(int((3000/fileLength)*(65536/8000)))]
x=np.linspace(0, (3000//fileLength), int((3000/fileLength)*(65536/8000)))
plt.subplot(224)
plt.plot(x, freqData_single, 'g')
plt.xlabel('(Hz)')
plt.title('FFT of the wave(part)')
plt.show()

f_observed = float(input('Enter the observed frequency(fft): '))
velovity = v_receiver(f_observed, 2000/(65536/8000), 0)
velovity_KmHr = velovity*3.6
print('Vehical velocity in km/hr:', velovity_KmHr)
