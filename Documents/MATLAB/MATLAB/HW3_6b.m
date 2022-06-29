clear;
close all;
clc;

Fs = 20000;
T = 1/Fs;
t = (1:64)*T;
x = 5*cos(2*pi*2000*t) + 4*cos(2*pi*2050*t);
X = fftshift(fft(x));
omega = ((-64/2):((64/2)-1))*2*pi*64;

plot(omega, abs(X), '-o')
title('|DFT| vs \Omega for 64 Samples')
xlabel('\Omega (rad/sample)')
ylabel('|DFT|')
xlim tight
ylim tight