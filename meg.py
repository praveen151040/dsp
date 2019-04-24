import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
fs,data=wav.read('gh.wav')
print(fs,len(data),data)
plt.subplot(211)
plt.plot(data)
t=np.arange((0,len(d)/fs,1.0/fs)
plt.subplot(212)
plt.plot(t,data)
plt.show()
wav.write('gh',0.5*fs,data)
