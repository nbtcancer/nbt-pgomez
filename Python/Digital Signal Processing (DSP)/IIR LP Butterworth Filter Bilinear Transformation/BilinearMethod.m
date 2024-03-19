%=============================================================
% IIR Filter using Bilinear Transformation - Butterworth N=3
% Author: Paul Gomez, PhD
% Date: March 18, 2024
%=============================================================
theta=0; 
delta=pi/200; 
i=1; 

while theta < 0.9*pi 
    Num = sqrt((1+3*cos(theta)+3*cos(2*theta)+cos(3*theta))^2 + (3*sin(theta)+3*sin(2*theta)+sin(3*theta))^2); 
    Den = sqrt((6+2*cos(2*theta))^2 + (2*sin(2*theta))^2); 
    H(i)= 20*log10(abs(Num/Den)); 
    w(i)=theta; 
    theta=theta+delta; 
    i=i+1; 
end 

% Plot the Frequency Response: 
plot(w,H); 
grid on; 
title('IIR Filter using Bilinear Transformation - Butterworth N=3'); 
ylabel('Amplitude Response (dB)'); 
xlabel('Frequency (radians)');
% *** THE END ***