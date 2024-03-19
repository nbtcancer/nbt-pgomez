# **************************************************************
# Butterworth IIR LP Filter using the Bilinear Transformation
# Paul Gomez, PhD
# March 18, 2024
# The equations used in this script are explained in the design
# document located on the same folder as this script.
# **************************************************************
from scipy import signal # not used
import numpy as np
import matplotlib.pyplot as plt

theta=0; 
delta=np.pi/200; 

H = np.array(0.00)
w = np.array(0.00)

i=1; 
while theta < 0.9 * np.pi:
    # filter numerator:
    Num = np.sqrt((1+3*np.cos(theta)+3*np.cos(2*theta)+np.cos(3*theta))**2 + (3*np.sin(theta)+3*np.sin(2*theta)+np.sin(3*theta))**2)
    # filter denominator:
    Den = np.sqrt((6+2*np.cos(2*theta))**2 + (2*np.sin(2*theta))**2)
    # Amplitude response:
    H = np.append(H,20*np.log10(abs(Num/Den)) )
    w = np.append(w,theta) 
    theta=theta+delta 
    i=i+1 
  

# Plot the Frequency Response: 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(w, H)
ax.set_title('IIR Filter using Bilinear Transformation - Butterworth N=3')
ax.set_xlabel('Frequency [Radians]')
ax.set_ylabel('Amplitude [dB]')
ax.grid(which='both', axis='both')

plt.show()

# *** end of program ***
