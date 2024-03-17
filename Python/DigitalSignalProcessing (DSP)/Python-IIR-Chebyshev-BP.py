# ********************************
# IIR Chebyshev Type II BP Filter
# ********************************
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# bandpass between 50 and 200 Hz
b, a = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*200], rs=60, btype='band', analog=True, ftype='cheby2')
w, h = signal.freqs(b, a, 1000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w / (2*np.pi), 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II Bandpass Frequency Response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()
# *** end of program ***
